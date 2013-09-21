__author__ = 'adam'

#import urllib
#import time
#from subprocess import Popen
#import shlex
#import os
import fusekiutils
import qudt4dt
import unittest

class TestQudt(unittest.TestCase):
    
    def setUp(self,result = None):
        self.barb = qudt4dt.Barbara("http://localhost:3030")
        
    def test_get_unit_class(self):
        self.assertEqual(self.barb.get_unit_class(u'http://qudt.org/vocab/unit#DegreeCelsius'),
                         [u'http://qudt.org/schema/qudt#TemperatureUnit'])

    def test_get_units_in_class(self):
        result = self.barb.get_units_in_class(u'http://qudt.org/schema/qudt#TemperatureUnit')
        units = [u'http://qudt.org/vocab/unit#DegreeFahrenheit',
                 u'http://qudt.org/vocab/unit#Kelvin',
                 u'http://qudt.org/vocab/unit#PlanckTemperature',
                 u'http://qudt.org/vocab/unit#DegreeCentigrade',
                 u'http://qudt.org/vocab/unit#DegreeCelsius',
                 u'http://qudt.org/vocab/unit#DegreeRankine']
        self.assertItemsEqual(result, units)
        
    def test_get_units_in_same_class(self):
        result = self.barb.get_units_in_same_class(u'http://qudt.org/vocab/unit#DegreeCelsius')
        units = [u'http://qudt.org/vocab/unit#DegreeFahrenheit',
                 u'http://qudt.org/vocab/unit#Kelvin',
                 u'http://qudt.org/vocab/unit#PlanckTemperature',
                 u'http://qudt.org/vocab/unit#DegreeCentigrade',
                 u'http://qudt.org/vocab/unit#DegreeCelsius',
                 u'http://qudt.org/vocab/unit#DegreeRankine']
        self.assertItemsEqual(result, units)
        
    def test_convert_value(self):
        convert_value = self.barb.convert_value
        degreeCelsius = u'http://qudt.org/vocab/unit#DegreeCelsius'
        degreeFahrenheit = u'http://qudt.org/vocab/unit#DegreeFahrenheit'
        inch = u'http://qudt.org/vocab/unit#Inc'
        temperatureUnit = u'http://qudt.org/schema/qudt#TemperatureUnit'
        
        self.assertAlmostEqual(convert_value(degreeCelsius,degreeFahrenheit,100),212.003333333)
       
        self.assertRaises(ValueError,convert_value,degreeFahrenheit,inch,300)
        
        self.assertRaises(ValueError,convert_value,temperatureUnit,degreeFahrenheit,300)

def main():
    try:
        print "launching fuseki..."
        fuseki = fusekiutils.LaunchFuseki()
        unittest.main()
        print ""
        
    finally:
        print "Terminating fuseki..."
        fuseki.terminate()

if __name__ == '__main__':
    main()
