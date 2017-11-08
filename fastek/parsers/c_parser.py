#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Comments"""

has_closing_tag = True

def check(mark):
    return mark == 'c'

def checkargs(mark,sline):
    args = sline.partition(';;c')[0]
    return len(args.split()) > 0

def main(**kw):
    line, text, i = kw['late_part'],kw['text'],kw['line_nb']
    if ';;c' not in line:
        for j, line2 in enumerate(text[i:]):
            j+=i
            if ';;c' not in line2:
                text[j] = ''
            else:
                text[j] = line2.partition(';;c')[2]
                break
    line = line.partition(';;c')[2]
    return line, text
        

