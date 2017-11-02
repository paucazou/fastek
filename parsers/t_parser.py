#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the 't' letter"""

import _shared

translators = {
    'c' : _shared.Translator("tc","","chapter"),
    's' : _shared.Translator("ts","","section"),
    'ss' : _shared.Translator("tss","","sub-section"),
    'p' : _shared.Translator("tp","","part"),
    'h' : _shared.Translator("th","","paragraph"),
    'hh': _shared.Translator("thh","","sub-paragraph"),
    }

def main(**kw):
    """Main function"""
    if kw['result'] == "latex":
        answer = _shared._tex_parser(**kw)
    return answer
