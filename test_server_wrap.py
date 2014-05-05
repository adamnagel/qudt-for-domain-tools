__author__ = 'adam'
import unittest
import socket
import time
from subprocess import Popen
import shlex
import os

from qudt4dt import sparql
import qudt4dt
import fusekiutils
import struct

def EnumerateAllUnitIndividuals():
    server_url = "http://localhost:3030"
    __url_query = server_url + '/qudt4dt/query?'

    # Fetch all unit individuals
    # SELECT -- return class and unit
    # WHERE -- First, get all subclasses of "Unit" (specific unit classes)
    #          Finally, get all individuals that are members of those classes (specific units)
    query = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT
    ?class ?unit
    WHERE
    { <http://qudt4dt.org/ontology#Unit> ^rdfs:subClassOf+ ?class .
      ?unit a ?class }
    """
    result = sparql.query(query, __url_query)
    bindings = result["results"]["bindings"]

    unit_individuals = []
    for x in bindings:
        url_unit = x["unit"]["value"]
        unit_individuals.append(url_unit)
        #print url_unit

    return unit_individuals


class TestServerWrap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # check/start fuseki
        try:
            fusekiutils.LaunchFuseki()
        except Exception:
            pass

        fp = open(os.devnull, 'w')
        cls._wrap = Popen(shlex.split('python qudt4dt/server/server_warp.py'), stdout=fp)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls._wrap.terminate()


def test_generator(url):
    def test(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('localhost', 3031))
        #time.sleep(2)
        unit = url
        send_len = len(unit)
        sock.send(struct.pack('!i', send_len) + unit)

        rec_len = sock.recv(struct.calcsize('!i'))
        rec_len = struct.unpack('!i', rec_len)[0]
        buf = ''
        count = 0
        while count < rec_len:
            _buf = sock.recv(1024)
            count += len(_buf)
            buf += _buf
        #print buf
        ins = qudt4dt.qudt_pb2.Unit()
        ins.ParseFromString(buf)
        sock.close()

        self.assertTrue(ins is not None)

    return test


if __name__ == '__main__':
    test_name = 'test_%s' % 'invalid_unit'
    test = test_generator('http://www.fakenamespace.org/thing#fakeunit')
    setattr(TestServerWrap, test_name, test)

    for t in EnumerateAllUnitIndividuals():
        test_name = 'test_%s' % t
        test = test_generator(t)
        setattr(TestServerWrap, test_name, test)

    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestServerWrap)
    unittest.TextTestRunner(verbosity=2).run(suite)

    print ""
    print "FAILURES: "
    print "=========="
    for failed in unittest.TestResult.failures:
        print failed
