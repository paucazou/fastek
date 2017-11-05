#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the "b" letter"""

import _shared

has_closing_tag = True

translators = {
    'i' : _shared.Translator("bi","textit","italic"),
    'u' : _shared.Translator("bu","","underlined"),
    'b' : _shared.Translator("bb","","bold"),
    }

def check(mark):
    """Checks if mark can be found in translators"""
    return mark[1] in translators

def checkargs(sline):
    """check if arguments are present, at least one"""
    return not ";;" in sline.split()[1]

def main(**kw):
    """Return correct answer"""
    if kw['result'] == "latex":
        answer = _shared._tex_parser(**kw,translators=translators)
    return answer


