import sys
sys.path.append("/usr/lib/python2.7/site-packages")
from qudt4dt.thrift.ttypes import *
from qudt4dt.thrift import Qudt4dt
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = Qudt4dt.Client(protocol)

  # Connect!
  transport.open()

  rs = client.query('http://qudt.org/vocab/unit#DegreeCelsius')
  print rs
  #print '4*5=%d' % (product)

  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)
