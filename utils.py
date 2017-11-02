#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module contains useful functions
not directly related to the purpose
of this program"""

def findall(string,chars):
    """Find all characters or string of characters
    contained in string.
    Return a list of indexes"""
    nb = len(chars) 
    return [ pos for pos, c in enumerate(string)
            if pos + nb <= len(string) and string[pos:pos + nb] == chars]

def underlineone(string,pos=-1,char='',printit=True):
    """Make a humanreadable emphasis under pos in string.
    If printit == True, print the result before returning it
    If char is not '', takes the first pos of char instead of pos"""
    if '\n' in string:
        raise SyntaxError("Please enter only one line")
    if char:
        pos = string.find(char)
    ns = " " * pos
    ns += "^"
    ns = string + '\n' + ns 
    if printit:
        print(ns)
    return ns

def underlineall(string,chars,printit=True):
    """Similar to underlineone, but put an emphasis under all chars
    if printit == True, print it before return it"""
    if '\n' in string:
        raise SyntaxError("Please enter only one line")
    pos = findall(string,chars)
    ns = ''
    j = 0
    lchars = len(chars)
    for i in pos:
        ns += ' '*(i-j) + "^"*lchars
        j=i+lchars
    ns = string + '\n' + ns
    if printit:
        print(ns)
    return ns
    
