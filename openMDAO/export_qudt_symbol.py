import sys
import os
sys.path.append(os.path.abspath('../'))
import qudt4dt
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
def get_all_unit_symbol():
    bara = qudt4dt.Barbara("http://localhost:3030")
    unitList = bara.list_all_units()
    result = {}
    for u in unitList:
        symbol = bara.get_SI_symbol(u)
        vec = bara.get_SI_vector(symbol)
        result[u] = vec
    return result

if __name__ == '__main__':
    for (k, v) in get_all_unit_symbol().items():
        print '%s\n %s\n' %(k,v)

