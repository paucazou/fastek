#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Checks the syntax"""

import utils

def checkfmark(mark,line,line_nb):
    """Checks if syntax of the first mark is correct, 
    i.e. has a space before and a space after
    mark is the mark itself (for example ,;np )
    with one character before and one after
    line is the complete line, line_nb her number in the text
    only useful if error
    return True if noerror, else raise exception
    """
    if False and mark[0] != ' ': # False, because specs have changed
        utils.underlineall(line,mark)
        raise SyntaxError("Please put a space before opening tag in line {}".format(line_nb))
    if mark[-1] != ' ':
        utils.underlineall(line,mark)
        raise SyntaxError("Please put a space after opening tag in line {}".format(line_nb))
    return True

def checklmark(mark,line,line_nb):
    """Similar to checkfmark, but for closing tag
    A closing tag must have no space before and one after"""
    if mark[0] == ' ':
        utils.underlineall(line,mark)
        raise SyntaxError("Please do not put a space before closing tag in line {}".format(line_nb))
    if False and mark[-1] != ' ': # always False, because specs have changed
        utils.underlineall(line,mark)
        raise SyntaxError("Please put a space after closing tag in line {}".format(line_nb))
    return True

def checkmark(mark,parser,line,line_nb):
    """Checks if mark exist.
    It can be an opening or a closing mark
    """
    if not parser.check(mark):
        utils.underlineall(line,mark)
        raise SyntaxError("{} is not allowed on line {}".format(mark,line_nb))
    return True

def checkargs(parser,mark,line_part,line,i):
    """Checks if arguments are correct"""
    if not parser.checkargs(mark,line_part):
        utils.underlineall(line,mark)
        raise SyntaxError("{} is not a correct arg for ,;{} on line {}".format(line_part,mark,i))
    return True
        
