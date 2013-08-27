import sys
import os
sys.path.append(os.path.abspath('modelica'))
import MSL2OWL

if __name__ == "__main__":
    p_ScriptPathRoot = os.path.dirname(__file__)
    
    ### Generate Modelica Unit Ontology
    p_SIUnits = os.path.join(p_ScriptPathRoot,'modelica/SIunits.mo')
    p_ModelicaUnitOntology = os.path.join(p_ScriptPathRoot,'modelica/modelica-individuals.xml')
    print "Generating Modelica Unit ontology"
    MSL2OWL.GenerateOWLIndividualFile(p_SIUnits,p_ModelicaUnitOntology)
    print "complete"