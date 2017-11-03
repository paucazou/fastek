#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Manages "v", to expand placeholders"""

import phlog
import utils

logger = phlog.loggers['console']

def main(text): # TODO mettre un warning en cas de fin de balise
    """Expand all placeholders.
    Syntax: ,;v name things to be stored\\n
    Please note that this function is case sensitive
    for placeholders and for their content"""
    names = {
            '::' + line.split()[1]:' '.join(line.split()[2:])
            for line in text if len(line) > 4 and line[:4] == ',;v '
            }
    ntext = []
    for i,line in enumerate(text):
        if len(line) > 4 and line[:4] == ',;v ':
            line = ''
        ntext.append(line)
        if ':: ' in line:
            utils.underlineall(line,":: ")
            raise SyntaxError("Please do not put a space after '::' in line {}".format(i))

    ntext = '§§§'.join(ntext)
    for name, text in names.items():
        ntext = ntext.replace(name,text)

    return ntext.split('§§§')

