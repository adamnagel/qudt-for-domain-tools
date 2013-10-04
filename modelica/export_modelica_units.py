__author__ = 'Zsolt'

import sys


from omc_session import OMCSession
import json


# def getBaseClasses(modelica_class, base_classes):
#     inheritance_cnt = ask_omc('getInheritanceCount', modelica_class)
#
#     for i in range(1, inheritance_cnt + 1):
#         base_class = ask_omc('getNthInheritedClass', modelica_class + ', ' + str(i))
#         getBaseClasses(base_class, base_classes)
#         base_classes.append(base_class)


def main():
    omc = OMCSession()

    success = omc.loadModel('Modelica')
    print success

    if success:
        modelica_classes = omc.getClassNames('Modelica.SIunits', recursive=True, qualified=True, sort=True)
        #print modelica_classes

        result = []
        for modelica_class in modelica_classes:
            info = {}
            info['name'] = modelica_class
            class_restriction = omc.getClassRestriction(modelica_class)
            info['class'] = class_restriction
            #info['text'] = omc.list(modelica_class)
            info['modifiers'] = {}
            print modelica_class
            modifiers = omc.getDerivedClassModifierNames(modelica_class)
            for modifier in modifiers:
                modifier_value = omc.getDerivedClassModifierValue(modelica_class, modifier)
                # ' = "value"' => 'value'
                modifier_value = modifier_value[3:].strip('"')
                info['modifiers'][modifier] = modifier_value

            result.append(info)

        with open('modelica_units.json', 'w') as f_p:
            json.dump(result, f_p)

if __name__ == '__main__':
    main()