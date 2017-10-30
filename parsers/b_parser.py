#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the "b" letter"""


def main(**kw):
    """Send data to the right function"""
    return functions[late_part[0]](late_part=kw['late_part'][1:],text=kw['text'],result=kw['result'])

def italic_parser(**kw):
    """Return italic mark in tex"""
    italic_part, mark, late_part = _endmark(kw['late_part'])
    return "\textit{" + italic_part + '}' + late_part

def underlined_parser(late_part,text,result):
    pass

def bold_parser(late_part,text,result):
    pass

def _endmark(line): # TODO fonction à mettre là où c'est nécessaire
    """Verifies if an endmark exists at the right place
    if True, return line.partition(',;')"""
    if ',;' in line.partition(',; '):# TODO ce n'est pas sûr du tout.
        raise SyntaxError("Marks are not correctly positioned in line {}".format(line)) # TODO add line number
    return line.partition(',;')

functions = {
        "i":italic_parser,
        "u":underlined_parser,
        " ": bold_parser,
        }
