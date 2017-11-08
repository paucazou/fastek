#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Parses file"""

import checker
import collections
import importlib
import indexer
import os
import phlog
import re
import sys
import utils

parsers_path = os.path.dirname(os.path.abspath(__file__)) + "/parsers/"
sys.path.append(parsers_path)

logger = phlog.loggers['console']
opening_mark = ",;"
closing_mark = ';;'
shabang = '#!/usr/bin/fastek' # TODO shaband must contain the type of document in arg : #!/usr/bin/fastek lesson
suffix = ".ftk"
parsers = {file[0]:importlib.import_module(file[:-3]) for file in os.listdir(parsers_path) if file[1:] == "_parser.py" in file
    } # a dict with a simple letter in key, and the module matching with it


def main(text,result="latex",check_text=True,index_project='',file_name=''): # TODO detect and make a warning for genuine latex marks
    """Main parsers. text is a string
    result : type of text returned :
    latex (default): translate fastek to latex
    raw : return raw text only
    check : if syntax is checked before. default : True
    index_project: the path of a project in order to save the names in an index.
    file_name is the name of the file containing the text"""
    if isinstance(text,str):
        text = text.split('\n')
        
    if check_text:
        check(text)
        
    print(text)
        
    ### managing placeholders
    text = parsers['v'].main(text)
    
    ### saving names
    if index_project:
        indexer.parse(text,index_project,file_name)
    
    
    for i in range(len(text)):
        line = text[i]
        ### managing end of line
        line = line.replace(" ,,","\\\\")
        
        while line.count(opening_mark):
            first_part, mark, late_part = line.partition(',;')
            if not late_part:
                break
            late_part, text = parsers[late_part[0]].main(late_part = late_part,
                                                   text=text,
                                                   result=result,
                                                   line_nb = i)
            line = first_part + late_part
        text[i] = line
    
    return '\n'.join(text)

def _load_file(path):
    """Loads an .ftk file and return it as a list of lines"""
    if path[:-4] != suffix:
        logger.warning("""{} has no {} suffix""".format(path,suffix))
    with open(file) as f:
        text = f.load().split('\n')
    
    if text[0].partition(' ')[0] != shabang:
        raise ValueError("{} is not a valid fastek file".format(path))
    return text

def check(text):
    """Check syntax of text
    text is a list or a listlike"""
    text = text.copy()
    if not isinstance(text,list): # TEST
        raise TypeError("text must be a listlike :\n{}".format(text))
    
    # managing latex genuine tag
    for i, line in enumerate(text):
        if '\\' in line:
            utils.underlineall(line,'\\')
            logger.warning("Genuine latex tags were found, but won't be evaluated on line {}".format(i))
    
    # check placeholders # TEST
    parsers['v'].check_syntax(text)
    
    for i,line in enumerate(text):
        # checking ends of lines TEST
        space_before_match = re.search("[^ ],,",line)
        if space_before_match:
            utils.underlineall(line,space_before_match.group())
            raise SyntaxError("Please put a space before EOL tag in line {}".format(i))
        space_after_match = re.search(",,[^ ]",line)
        if space_after_match:
            utils.underlineall(line,space_after_match.group())
            raise SyntaxError("Please put a space or a carriage return after EOL tag in line {}".format(i))
        
        # checking illegal closing tags TEST
        for parser, module in parsers.items():
            if not module.has_closing_tag:
                if closing_mark + parser in line:
                    utils.underlineall(line,closing_mark+parser)
                    raise SyntaxError("{} parser has no closing tag: check line {}".format(parser,i))
        
        # checking other tags
        if opening_mark in line:
            fline,nothing, sline = line.partition(opening_mark)
            while True:
                # checking each sub parser
                mark_to_test = sline.split()[0]
                parser = parsers[mark_to_test[0]]
                checker.checkmark(mark_to_test,parser,line,i)
                checker.checkargs(parser,mark_to_test,sline,line,i)
                
                # checking closing tag TEST BUG
                if parser.has_closing_tag:
                    closing_tag = closing_mark + mark_to_test
                    opening_tag = opening_mark + mark_to_test
                    if opening_tag in sline:
                        utils.underlineall(sline,opening_tag)
                        raise SyntaxError("{} opening tag has been found before closing tag expected on line {}".format(opening_tag,i))
                    if closing_tag in sline:
                        part1,tag,part2 = sline.partition(closing_tag)
                        sline = part1 + part2
                    else: # looking for closing tag in the rest of the text
                        for j,line2 in enumerate(text[i+1:]):
                            j+=i+1
                            fline2, mark_expected, sline2 = line2.partition(closing_tag)
                            if opening_tag in fline2:
                                print("Opening tag not closed, line {}".format(i))
                                print(fline,nothing,utils.underlineall(sline,opening_tag,False))
                                print("Opening tag found too soon, line {}".format(j))
                                utils.underlineall(line2,opening_tag)
                                raise SyntaxError("{} opening tag has been found before closing tag expected".format(opening_tag))
                            if mark_expected:
                                text[j] = fline2 + sline2
                                break
                        else:
                            print(fline,nothing,utils.underlineall(sline,opening_tag,False))
                            raise SyntaxError("No closing tag found for {} in line {}".format(opening_tag,i))
                new_partition = sline.partition(opening_mark)
                fline = fline + nothing + new_partition[0]
                nothing, sline = new_partition[1:]
                    
                if opening_mark not in sline: # condition to break loop
                    line = fline + nothing + sline
                    break
        
        # checking alone closing tags -> closing tags are supposed to be deleted TEST
        if closing_mark in line: 
            alone_closing_tag = utils.wrappedchars(line,closing_mark)
            utils.underlineall(line,alone_closing_tag)
            raise SyntaxError("An only closing tag has been found in line {}".format(i))
    
    return True
            
        
    


