#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the "b" letter"""


def main(late_part,text,result):
    """Send data to the right function"""
    return functions[late_part[0]](late_part[1:],text,result)

def italic_parser():
    """Return italic mark in tex"""
    pass

def underlined_parser():
    pass

def bold_parser():
    pass

functions = {
        "i":italic_parser,
        "u":underlined_parser,
        " ": bold_parser,
        }
