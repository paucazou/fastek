#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Parses file"""

import check
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


def main(text,result="latex",index_project='',file_name=''): # TODO detect and make a warning for genuine latex marks
    """Main parsers. text is a string
    result : type of text returned :
    latex (default): translate fastek to latex
    raw : return raw text only
    index_project: the path of a project in order to save the names in an index.
    file_name is the name of the file containing the text"""
    if isinstance(text,str):
        text = text.split('\n')
        
    ### managing placeholders
    text = parsers['v'].main(text)
    
    ### saving names
    if index_project:
        indexer.parse(text,index_project,file_name)
        
    ### managing latex genuine tag
    for line in text:
        if '\\' in line:
            logger.warning("Genuine latex tags were found, but won't be evaluated : ")
            utils.underlineall(line,'\\')
            
    for i,line in enumerate(text):
        line_before = line
        
        ### managing end of line
        line = line.replace(" ,,","\\\\")
        if ",," in line:
            utils.underlineone(line,char=',,')
            raise SyntaxError("Please put a space before ,, in line {} : {}".format(i,line_before))
        
        while line.count(opening_mark):
            first_part, mark, late_part = line.partition(',;')
            if not late_part:
                break
            late_part = parsers[late_part[0]].main(late_part = late_part,
                                                   text=text,
                                                   result=result,
                                                   line_nb = i)
            line = first_part + late_part
        if closing_mark in line:
            raise SyntaxError("A closing tag has no opening tag in line {} : {}".format(i,line_before))
        text[i] = line
    
    return '\n'.join(ntext)

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
    if not isinstance(text,list):
        raise TypeError("text must be a listlike :\n{}".format(text))
    
    # check placeholders
    parsers['v'].check(text)
    
    for i,line in enumerate(text):
        # checking ends of lines
        space_before_match = re.search("[^ ],,",line)
        if space_before_match:
            utils.underlineall(line,space_before_match.group())
            raise SyntaxError("Please put a space before EOL tag in line {}".format(i))
        space_after_match = re.search(",,[^ ]",line)
        if space_after_match:
            utils.underlineall(line,space_after_match.group())
            raise SyntaxError("Please put a space or a carriage return after EOL tag in line {}".format(i))
        
        # checking illegal closing tags
        for parser, module in parsers.items():
            if not module.has_closing_tag:
                if closing_mark + parser in line:
                    utils.underlineall(line,closing_mark+parser)
                    raise SyntaxError("{} parser has no closing tag: check line {}".format(parser,i))
     
    
        
    


