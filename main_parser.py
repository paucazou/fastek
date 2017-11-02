#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Parses file"""

import importlib
import os
import phlog
import sys

parsers_path = os.path.dirname(os.path.abspath(__file__)) + "/parsers/"
sys.path.append(parsers_path)

logger = phlog.loggers['console']
opening_mark = ",;"
closing_mark = ';;'
shabang = '#!/usr/bin/fastek' # TODO shaband must contain the type of document in arg : #!/usr/bin/fastek lesson
suffix = ".ftk"
parsers = {file[0]:importlib.import_module(file[:-3]) for file in os.listdir(parsers_path) if file[1:] == "_parser.py" in file
    } # a dict with a simple letter in key, and the module matching with it

def main(text,result="latex"): # TODO detect and make a warning for genuine latex marks
    """Main parsers. text is a string
    result : type of text returned :
    latex (default): translate fastek to latex
    raw : return raw text only"""
    if isinstance(text,str):
        text = text.split('\n')
    ntext = []
    for i,line in enumerate(text):
        line_before = line
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
        ntext.append(line) # TODO traitement de la fin de ligne
    
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
        
    


