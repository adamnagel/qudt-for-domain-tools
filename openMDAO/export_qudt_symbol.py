# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('../'))
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 


import re
import qudt4dt
bara = qudt4dt.Barbara("http://localhost:3030")
baseUnit = {u'L':u'm', u'M':u'kg',
            u'T':u's', u'I':u'A',
            u'N':u'mol',u'J':u'cd',
            u'\u0398': u'K', u'U':u'rad'}

def symbol_lex_token(symbolString):
    if symbolString == '':
        return []
    else:
        token = re.compile(ur'^([LMNJTIU\u0398])-?\d*',re.UNICODE)
        result = re.match(token,symbolString)
        point = len(result.group(0))
        power = result.group(0)[len(result.group(1)):]
        pair = (result.group(1), power)
        return symbol_lex_token(symbolString[point:]) + [pair]
        
def tokens_to_unit(tokens):
    r = ''
    for (i,j) in tokens:
        if j == '':
            r += '*{sym}'.format(sym = baseUnit[i])
        else:
            r += '*{sym}**{pow}'.format( sym = baseUnit[i], pow =j)
    return r[1:]

def get_all_unit_symbol():
    unitList = bara.list_all_units()
    result = {}
    for u in unitList:
        symbol = bara.get_SI_symbol(u)

        if not symbol == None:
            print u
            si = re.match(r'http://qudt.org/vocab/dimension#Dimension_SI_(.+)$',symbol).group(1)
            print si
            print tokens_to_unit(symbol_lex_token(si))
            print ('\n')
       # vec = bara.get_SI_vector(symbol)
       # print vec

if __name__ == '__main__':
    # print u'\u0398'
    get_all_unit_symbol()
    #print tokens_to_unit(symbol_lex_token(u'ϴ-1'))
   # print bara.get_unit_class('http://qudt.org/vocab/unit#SquareCentimeterMinute')
   # print bara.get_units_in_same_class('http://qudt.org/vocab/unit#SquareCentimeterMinute')
