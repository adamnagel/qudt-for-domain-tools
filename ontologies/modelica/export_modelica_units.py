__author__ = 'Zsolt'

from omc_session import OMCSession
import json
import argparse
import os

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

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--library", help="External library to load.")
    parser.add_argument("-p", "--package", help="Package name to parse like: Modelica.SIunits",
                        default="Modelica.SIunits")
    args = parser.parse_args()

    omc = OMCSession()
    
    print "Loading Modelica library ..."
    success = omc.loadModel('Modelica')    
    if success:
        print "[OK]"
    else:
        print "[FAILED]"
        return
        
    if args.library:
        print "Loading External library {0} ...".format(args.library)
        cwd = os.getcwd()
        dir_name = os.path.dirname(args.library)
        os.chdir(dir_name)
        success = success and omc.loadFile(args.library)
        os.chdir(cwd)
        if success:
            print "[OK]"
        else:
            print "[FAILED]"

    if success:
        print "Getting all class names for package: {0}".format(args.package)
        modelica_classes = omc.getClassNames(args.package, recursive=True, qualified=True, sort=True)
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

            getBaseClassModifiers(omc, modelica_class, info['modifiers'])

            result.append(info)
        
        output_filename = 'modelica_units.json'
        with open(output_filename, 'w') as f_p:
            json.dump(result, f_p)
        
        print 'File was generated: {0}'.format(output_filename)
if __name__ == '__main__':
    main()