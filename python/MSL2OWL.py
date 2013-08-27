'''
Created on Aug 13, 2013

@author: adam
'''

import re
import json

def ExtractUnitsFromMSL(p_mslSIUnits):
    # Read contents of SIunits.mo
    f_mslSIUnits = open(p_mslSIUnits,'r')
    as_mslSIUnits_ = f_mslSIUnits.readlines()
    f_mslSIUnits.close()
        
    # Remove comment lines
    s_mslSIUnits = ''
    for s in as_mslSIUnits_:
        if s.find('//') == -1:
            s_mslSIUnits += s
        
    # Strip out whitespace
    s_mslSIUnits = s_mslSIUnits.replace('\n','').replace('\r','').replace('\t','').replace('  ','')
    
    # Divide into lines based on semicolon
    d_TypeStatements = dict()
    as_Statements = s_mslSIUnits.split(';')
    pr_IsTypeStatement = re.compile('type.*')
    for s in as_Statements:
        
        mo_IsTypeStatement = pr_IsTypeStatement.match(s)
        if mo_IsTypeStatement != None:
            mo = re.match(r"type (?P<type_name>\w+)",s)
            key = mo.group(1)
            
            d_TypeStatements[key] = GetUnitPropDict(s)
            d_TypeStatements[key]['ClassPath'] = 'Modelica.SIunits.' + key
                    
    return d_TypeStatements
            
def CombineDict(d1, d2):
    return dict(d1.items() + d2.items())

# RegEXes for unit properties
apr_DataTypeProps = []
apr_DataTypeProps.append( re.compile('.*=\s*(?P<UnitDataType>\w+) ') )
apr_DataTypeProps.append( re.compile('.*final quantity\s*=\s*\"(?P<UnitQuantity>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*final unit\s*=\s*\"(?P<UnitUnit>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*displayUnit\s*=\s*\"(?P<UnitDisplayUnit>\w+)\"') )
apr_DataTypeProps.append( re.compile('.*min\s*=\s*(?P<UnitMin>\w+)') )
apr_DataTypeProps.append( re.compile('.*start\s*=\s*(?P<UnitStart>\w+)') )
pr_EquivalentClass = re.compile('type \S*\s*=\s*(?P<EquivalentClass>\w+)')
def GetUnitPropDict(str):
    d_rtn = dict()
        
    for pr in apr_DataTypeProps:
        if pr.match(str) != None:
            d_rtn = CombineDict(d_rtn,pr.match(str).groupdict())
    
    if str.find('(') == -1:
        # This is just equivalent to something else
        d_rtn = CombineDict(d_rtn, pr_EquivalentClass.match(str).groupdict())
    
    return d_rtn


if __name__ == '__main__':
    d_TypeStatements = ExtractUnitsFromMSL("../../ModelicaStandardLibrary/Modelica 3.2/SIunits.mo")
    
    print json.dumps(d_TypeStatements, sort_keys=True,indent=4)