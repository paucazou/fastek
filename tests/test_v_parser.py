#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
import sys
sys.path.append('./fastek')
import fastek.parsers.v_parser as vp
import pytest

def test_closing_tag():
    assert vp.has_closing_tag == False

def test_check_syntax():
    text = [',;vt can\'t work']
    with pytest.raises(SyntaxError): # unknown tag
        vp.check_syntax(text)

    text = [",;v "]
    with pytest.raises(SyntaxError): # no placeholder
        vp.check_syntax(text)

    text = """,;v placeholderalone """.split("\n")
    with pytest.raises(SyntaxError): # no value
        vp.check_syntax(text)

    text = """,;v placeholder something
    :: placeholder""".split("\n")
    with pytest.raises(SyntaxError): # space after ::
        vp.check_syntax(text)

    text = """::nameunknown """.split("\n")
    with pytest.raises(NameError): # name unknown
        vp.check_syntax(text)

    text = """,;v one Un jeune garçon vint au village ,, et trouva une fleur.
    ::one ::one ,,
    """.split('\n')
    assert vp.check_syntax(text) == True

def test_main():
    text = """,;v jean Évangile selon St Jean
::jean""".split('\n')
    assert vp.main(text) == ['', 'Évangile selon St Jean']

def test_check():
    assert vp.check('v')
