#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""This module manages the "b" letter"""

import _shared

translators = {
    'i' : _shared.Translator("bi","\textit","italic"),
    'u' : _shared.Translator("bu","","underlined"),
    'b' : _shared.Translator("bb","","bold"),
    }


def main(**kw):
    """Return correct answer"""
    if kw['result'] == "latex":
        answer = _shared._tex_parser(**kw)
    return answer


