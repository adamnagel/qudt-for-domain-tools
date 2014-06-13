import sys 
sys.path.append("../../")
import socket  
import time 
import qudt4dt
import struct
def get_instance(url):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect(('localhost', 3031))  
    time.sleep(2)  
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
    
    ins = qudt4dt.qudt_pb2.Unit()
    ins.ParseFromString(buf)
    sock.close() 
    return ins
    
def from_qudt_to_modelica(url):
    tmp = get_instance(url)
    return tmp.modelica_unit

def value_conversion(src_url, obj_url, value):
    src = get_instance(src_url)
    obj = get_instance(obj_url)
    if src.qudt_unit.offset == '' or src.qudt_unit.factor == '' \
        or obj.qudt_unit.offset == '' or obj.qudt_unit.factor == '':
            raise RuntimeError("the runtime error raised")
    src_offset = float(src.qudt_unit.offset)
    src_factor = float(src.qudt_unit.factor)
    obj_offset = float(obj.qudt_unit.offset)
    obj_factor = float(obj.qudt_unit.factor)
    return ((src_offset - obj_offset) + float(value)) * src_factor / float(obj_factor)
    
if __name__ == '__main__':
    fack = u'http://www.fakenamespace.org/thing#fakeunit'
    #t = get_instance(fack)
    meter = u'http://qudt.org/vocab/unit#Meter'
    m_unit = from_qudt_to_modelica(meter)
    print m_unit.url
    print m_unit.classPath
    print '-------------------------------------------------------------'
    centimeter= u'http://qudt.org/vocab/unit#Centimeter'

    print value_conversion(meter, centimeter, 10)