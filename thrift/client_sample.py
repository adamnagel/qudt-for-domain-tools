import sys
sys.path.append("./gen-py/thrift")
from qudt4dt.thrift.ttypes import *
from qudt4dt.thrift import Qudt4dt_base
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TJSONProtocol


try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TJSONProtocol.TJSONProtocol(transport)

  # Create a client to use the protocol encoder
  client = Qudt4dt_base.Client(protocol)

  # Connect!
  transport.open()

  meter = client.query('http://qudt.org/vocab/unit#Meter')
  print meter
  one_meter = Quantity(meter, 1)
  x_inch = client.quantity_convert(one_meter, 'http://qudt.org/vocab/unit#Inch')
  print x_inch

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)