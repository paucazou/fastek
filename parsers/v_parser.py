#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Manages "v", to expand placeholders"""

import checker
import phlog
import re
import utils

logger = phlog.loggers['console']

has_closing_tag = False

def check(mark):
    """check if mark is allowed"""
    if mark != "v":
        return False
    return True

def check_syntax(text):
    """Checks the syntax correctness
    Return True if all is good
    WARNING this function does not check
    possible illegal closing tags"""
    
    names = []
    for i,line in enumerate(text):
        # check names declaration
        
        if ',;v' in line:
            mark = utils.wrappedchars(line,',;v')
            checker.checkfmark(mark,line,i)
            line_spl = line.split()
            if line_spl[0] != ',;v':
                raise SyntaxError("Unknown tag '{}' on line {}".format(line_spl[0],i))
            try:
                names.append(line_spl[1])
            except IndexError:
                utils.underlineall(line,',;v')
                raise SyntaxError("There's no placeholder after opening tag ,;v in line {}".format(i))
            try:
                assert len(line_spl) > 2
            except AssertionError:
                utils.underlineall(line,line_spl[1])
                raise SyntaxError("No value given to '{}' at line {}".format(line_spl[1],i))
            
        # check expansion
        if "::" in line:
            # spaces
            if ":: " in line:
                utils.underlineall(line,":: ")
                raise SyntaxError("Please do not put a space after '::' in line {}".format(i))
            space_before_match = re.search("[^ ]::",line)
            if space_before_match:
                utils.underlineall(line,space_before_match.group())
                raise SyntaxError("Please put a space before '::' or start the line with it in line {}".format(i))
            # is the name already saved ?
            sline = line.partition("::")[2]
            while sline:
                name_checked = sline.split()[0]
                if  name_checked not in names:
                    utils.underlineall(line,name_checked)
                    raise NameError("There is no name '{}' in line {}".format(name_checked,i))
                sline = sline.partition("::")[2]
    return True   

def main(text):
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

    ntext = '§§§'.join(ntext)
    for name, text in names.items():
        ntext = ntext.replace(name,text)

    return ntext.split('§§§')

