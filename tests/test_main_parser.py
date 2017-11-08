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

@mock.patch("checker")
def test_check(mchecker):
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
    
    # closing tag before opening tag
    text = """;;c""".split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)
        
    # closing tag before opening tag
    # even if an opening is in the line
    text = """;;c ,;c""".split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)
        
    # closing tag missing
    text = """,;c """.split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)
        
    # closing tag missing with more than one line
    text = """,;c
    
    """.split("\n")
    with pytest.raises(SyntaxError):
        fmp.check(text)
        
    # new opening tag before closing tag
    text = """,;c ,;c ;;c""".split()
    with pytest.raises(SyntaxError):
        fmp.check(text)
        
    # test if checker has been called
    mchecker.reset()
    text = """,;c and so ;;c""".split("\n")
    fmp.check(text)
    mchecker.checkmark.assert_called_once_with(fmp.parsers['c'],',;c'," and so ;;c",",;c and so ;;c",0)



