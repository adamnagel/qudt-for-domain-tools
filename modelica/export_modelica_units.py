__author__ = 'Zsolt'

from omc_session import OMCSession
import json


def getBaseClassModifiers(omc, modelica_class, info_modifiers):
    inheritance_cnt = omc.getInheritanceCount(modelica_class)

    for i in range(1, inheritance_cnt + 1):
        base_class = omc.getNthInheritedClass(modelica_class, i)

        modifiers = omc.getDerivedClassModifierNames(modelica_class)
        for modifier in modifiers:
            if modifier in info_modifiers:
                # use override
                continue

            # use base class' value
            modifier_value = omc.getDerivedClassModifierValue(modelica_class, modifier)
            # ' = "value"' => 'value'
            modifier_value = modifier_value[3:].strip('"')
            info_modifiers[modifier] = modifier_value

        getBaseClassModifiers(omc, base_class, info_modifiers)


def main():
    omc = OMCSession()

    success = omc.loadModel('Modelica')
    print success

    if success:
        modelica_classes = omc.getClassNames('Modelica.SIunits', recursive=True, qualified=True, sort=True)
        #print modelica_classes

        result = []
        for modelica_class in modelica_classes:
            if modelica_class == 'Modelica.SIunits.IsothermalCompressibility':
                print modelica_class + ' STOP HERE'
                v = omc.typeNameStrings(modelica_class)
                print v
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

            getBaseClassModifiers(omc, modelica_class, info['modifiers'])

            result.append(info)

        with open('modelica_units.json', 'w') as f_p:
            json.dump(result, f_p)

if __name__ == '__main__':
    main()