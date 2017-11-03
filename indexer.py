#!/usr/bin/python3
# -*-coding:Utf-8 -*
#Deus, in adjutorium meum intende
"""Save names into an index
    Each pickle file has this structure:
    {'person':{
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
marks = {'p':Mark("p","person",1),
        'l':Mark("l","place",1),
        't':Mark("t","town",1),
        "e":Mark("e","people",2)
        }



def parse(text,index,file_name):
    """Looks for new names to save in text
    Save new line number for already saved names
    index is the path of the file containing the index
    file_name is the name of the file of text
    return text cleaned"""
    # load data
    with open(index,'br') as f:
            data = pickle.Unpickler(f).load()
    # look for new names
    for i,line in enumerate(text):
        if main_mark in line:
            text[i], data = _detect_marks(line,line_nb,data)

    # saving new linenumbers
    for category,value in data.items():
        for names in value:
            if category == 'people':
                value[name][file_name] = [i for i,line in enumerate(text) if name[0] in line or name[1] in line]
            else:
                value[name][file_name] = [i for i,line in enumerate(text) if name in line]

    # saving data into file
    with open(index,'bw') as f:
        pickle.Pickler(f).dump(data)
    
    return text

def _detect_marks(line,line_nb,index_data):
    """Detects (possibly) new names to index
    return the index_data modified
    and the line cleaned
    """
    while main_mark in line:
        fpart,mark,lpart = line.partition(main_mark)
        try:
            category = marks[lpart[0]]
        except KeyError:
            raise SyntaxError("Unknow mark") # TODO faire un module d'erreurs et l'appeler
        lpart = lpart.split()[1:]
        if category.words_nb > 1:
            name = tuple(lpart[:category.words_nb])
        else:
            name = lpart[0]
        data[category.human_name].setdefault(name)
        
        line = fpart + ' '.join(lpart)
    
    return line, data

