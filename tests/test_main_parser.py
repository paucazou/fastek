#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
import sys
sys.path.append('./fastek')
import fastek.main_parser as fmp
import pytest
import unittest.mock as mock

fmp.parsers = {'v':mock.MagicMock(),'o':mock.MagicMock(),'c':mock.MagicMock()}
fmp.parsers['o'].has_closing_tag= False
fmp.parsers['c'].has_closing_tag= True

def test_check():
    # text not a list
    text = """text """
    with pytest.raises(TypeError):
        fmp.check(text)

    # no space before ,,
    text = """No space,, """.split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)

    # call to v_parser
    fmp.parsers['v'].check_syntax.assert_called_once_with(text)
    # no space after ,,
    text = """eol ,,no space """.split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)

    # illegal closing tag
    text = """,;o something ;;o""".split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)

    # legal closing tag
    text = """,;c something ;;c""".split("\n")
    assert fmp.check(text) == True




