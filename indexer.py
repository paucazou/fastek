#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Save names into an index
    Each pickle file has this structure:
    {'persons':{
        NAME:{
            FILE_NAME:[line,line,line...]
            },
        NAME:{...},
        },
    'place':{...},
    'town':{...},
    'people':{
        (NAME_sg,NAME_pl):{...},
        },
    }
    """

import collections
import pickle

main_mark = ",;n"
Mark = collections.namedtuple("Marks",("mark","human_name",'words_nb'))
marks = {main_mark+'p':Mark("p","person",1),
        main_mark+'l':Mark("l","place",1),
        main_mark+'t':Mark("t","town",1),
        main_mark+"e":Mark("e","people",2)
        }



def parse(text,index,file_name):
    """Looks for new names to save in text
    Save new line number for already saved names
    index is the path of the file containing the index
    file_name is the name of the file of text"""
    # load data
    with open(index,'br') as f:
            data = pickle.Unpickler(f).load()
    # look for new names
    for i,line in enumerate(text):
        if main_mark in line:
            data = _detect_marks(line,data)

    # saving new linenumber
    for category,value in data.items():
        for name in value:
            value[name][file_name] = [i for i,line in enumerate(text) if name in line] # BUG ne marchera pas avec le tuple pour les nations


def _detect_marks(line,index_data):
    """Detects (possibly) new names to index
    return the index_data modified (if necessary)
    """
    pass

