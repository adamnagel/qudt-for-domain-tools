import sys
import os
sys.path.append(os.path.abspath('../'))
import qudt4dt
def get_all_unit_symbol():
    bara = qudt4dt.Barbara("http://localhost:3030")
    unitList = bara.list_all_units()
    result = {}
    for u in unitList:
        symbol = bara.get_units_symbol(u)
        if symbol == []:
            continue
        else:
            result[u] = bara.get_units_symbol(u)
    return result

if __name__ == '__main__':
    for (k, v) in get_all_unit_symbol().items():
        print '%s \t %s\n' %(k,v)
