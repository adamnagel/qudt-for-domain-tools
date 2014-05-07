__author__ = 'adam'
import unittest
import socket
from subprocess import Popen
import shlex
import os
from multiprocessing import Pool
import time

from qudt4dt import sparql
import qudt4dt
import fusekiutils
import struct

def EnumerateAllUnitIndividuals(server_url):
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
    pass


def test_generator(url):
    def test_unit(self):
        ins = test_url(url)
        self.assertTrue(ins is not None)

    return test_unit


def test_url(url):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect(('localhost', 3031))
    #time.sleep(2)
    unit = url
    send_len = len(unit)
    sock.send(struct.pack('i', send_len) + unit)

    rec_len = sock.recv(struct.calcsize('i'))
    rec_len = struct.unpack('i', rec_len)[0]
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

    return ins


def perf_benchmark_generator(AllUnits):
    def test_performance(self):
        p = Pool(5)
        start_time = time.time()

        p.map(test_url, AllUnits)

        elapsed = time.time() - start_time
        print "Elapsed: %02d seconds" % elapsed
        return elapsed

    return test_performance


if __name__ == '__main__':
    # Launch fuseki
    fusekiutils.LaunchFuseki()

    # Launch server wrap
    fp = open(os.devnull, 'w')
    server_wrap = Popen(shlex.split('python server_warp.py'), cwd="qudt4dt/server/", stdout=fp)
    time.sleep(2)

    try:
        test_name = 'test_%s' % 'invalid_unit'
        test = test_generator('http://www.fakenamespace.org/thing#fakeunit')
        setattr(TestServerWrap, test_name, test)

        server_url = "http://localhost:3030"

        all_units = EnumerateAllUnitIndividuals(server_url)
        for t in all_units:
            test_name = 'test_%s' % t
            test = test_generator(t)
            setattr(TestServerWrap, test_name, test)

        test_performance_func = perf_benchmark_generator(all_units)
        setattr(TestServerWrap, "test_performance", test_performance_func)

        unittest.main()
        suite = unittest.TestLoader().loadTestsFromTestCase(TestServerWrap)
        unittest.TextTestRunner(verbosity=2).run(suite)

        print ""
        print "FAILURES: "
        print "=========="
        for failed in unittest.TestResult.failures:
            print failed

    finally:
        server_wrap.terminate()
