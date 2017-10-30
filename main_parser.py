#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Parses file"""

import importlib
import os
import sys

parsers_path = os.path.dirname(os.path.abspath(__file__)) + "/parsers/"
sys.path.append(parsers_path)

mark = ",;"
parsers = {file[0]:importlib.import_module(file[:-3]) for file in os.listdir(parsers_path) if file[1:] == "_parser.py" in file
    } # a dict with a simple letter in key, and the module matching with it

def main(file,result="latex"):
    """Main parsers. file is a path with .ftk suffix TODO verify this
    result : type of text returned :
    latex (default): translate fastek to latex
    raw : return raw text only"""
    with open(file) as f:
        text = f.load().split('\n')
    ntext = []

    for line in text:
        mark_count = line.count(mark)
        for i in range(mark_count):
            first_part, mark, late_part = line.partition(',;')
            if not late_part:
                break
            late_part = parsers[late_part[0]].main(late_part[1:],text,result)
            line = first_part + late_part
        ntext.append(line) # TODO traitement de la fin de ligne
    
    return '\n'.join(ntext)


