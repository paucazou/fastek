#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the 't' letter"""

import _shared
import phlog
import utils

logger = phlog.loggers['console']

has_closing_tag = False
# TODO intégrer \chapter*{}

translators = {
    'c' : _shared.Translator("tc","chapter","chapter"), # WARNING indisponible pour docs article et letter. Que faire ? Un warning ? Un refus ?
    's' : _shared.Translator("ts","section","section"),
    'u' : _shared.Translator("tss","subsection","sub-section"),
    'p' : _shared.Translator("tp","part","part"),
    'h' : _shared.Translator("th","paragraph","paragraph"),
    'r': _shared.Translator("thh","subparagraph","sub-paragraph"),
    }

def main(**kw):
    """Main function"""
    
    if ';;' + translators[kw['late_part'][1]].mark in kw['late_part']:
        logger.warning("Closing tag is useless with titles on line {} :".format(kw['line_nb']))
        print(';;' + kw['late_part'][:2])
        utils.underlineall(kw['text'][kw['line_nb']],';;' + kw['late_part'][:2])
    if kw['result'] == "latex":
        answer = _shared._tex_parser(**kw,translators=translators)
    return answer
