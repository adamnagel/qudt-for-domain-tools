__author__ = 'Zsolt'

import OMPython
import json

omc_cache = {}


def ask_omc(question, opt=None, parsed=True):
    p = (question, opt, parsed)
    if p in omc_cache:
        return omc_cache[p]

    if opt:
        expression = question + '(' + opt + ')'
    else:
        expression = question

    #logger.debug('ask_omc: {0}  - parsed: {1}'.format(expression, parsed))

    try:
        if parsed:
            res = OMPython.execute(expression)
        else:
            res = OMPython.omc.sendExpression(expression)
    except Exception as e:
        print "OMC failed: {0}, {1}, parsed={2}".format(question, opt, parsed)
        raise e

    omc_cache[p] = res

    return res


def getBaseClasses(modelica_class, base_classes):
    inheritance_cnt = ask_omc('getInheritanceCount', modelica_class)

    for i in range(1, inheritance_cnt + 1):
        base_class = ask_omc('getNthInheritedClass', modelica_class + ', ' + str(i))
        getBaseClasses(base_class, base_classes)
        base_classes.append(base_class)


def main():
    success = ask_omc('loadModel', 'Modelica')
    print success

    if success:
        modelica_classes = ask_omc('getClassNames', 'Modelica.SIunits, recursive=true, qualified=true, sort=true')['SET1']['Set1']
        #print modelica_classes

        result = []
        for modelica_class in modelica_classes:
            info = {}
            info['name'] = modelica_class
            class_restriction = ask_omc('getClassRestriction', modelica_class).strip().strip('"')
            info['class'] = class_restriction
            info['text'] = ask_omc('list', modelica_class)
            info['modifiers'] = []
            print modelica_class

            base_classes = []
            getBaseClasses(modelica_class, base_classes)

            for base_class in base_classes:
                modifier = {}
                modifier['className'] = base_class
                modifier['values'] = []
                answer = ask_omc('getExtendsModifierNames', modelica_class + ',' + base_class)
                if not 'SET1' in answer:
                    print 'skip: {0}'.format(answer)
                    continue
                elif not 'Set1' in answer['SET1']:
                    print 'skip: {0}'.format(answer)
                    continue

                keys = answer['SET1']['Set1']
                for key in keys:
                    value = ask_omc('getExtendsModifierValue', modelica_class + ',' + base_class + ',' + key)
                    modifier['values'].append({'name': key, 'value': value})
                    #print (key, value)

                info['modifiers'].append(modifier)

            result.append(info)

        with open('modelica_units.json', 'w') as f_p:
            json.dump(result, f_p)

if __name__ == '__main__':
    main()