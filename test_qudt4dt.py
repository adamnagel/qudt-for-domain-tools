__author__ = 'adam'

import qudt4dt

barb = qudt4dt.Barbara("http://localhost:3030")
print barb.get_server_status()
print ""


print "Get Unit Class"
print barb.get_unit_class("Unit1")
print ""

print "Get Units in Class"
print barb.get_units_in_class("Unit1")
print ""

print "Get Units in Same Class"
print barb.get_units_in_same_class("Unit1")
print ""

print "Convert Value"
print barb.convert_value("Unit1","Unit2",3.4)