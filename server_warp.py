import socket
import qudt4dt



def create_message(url):
    url_base = 'http://localhost:3030'
    q = qudt4dt.qudt.QudtUnit(url_base, url)
    mdao = qudt4dt.mdao.MdaoUnit(url_base, url)
    mode = qudt4dt.modelica.ModelicaUnit(url_base, url)
    instance = qudt4dt.qudt_pb2.Unit()
    tmp = qudt4dt.qudt_pb2.Unit()
    q.createInstance(tmp.qudt_unit)
    mode.createInstance(tmp.modelica_unit)
    mdao.createInstance(tmp.mdao_unit)
    return tmp

def daemon():
    unit = u'http://qudt.org/vocab/unit#Meter'
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.bind(('localhost', 3031))  
    sock.listen(5)  
    while True:  
        connection,address = sock.accept()  
        try:  
            connection.settimeout(5)  
            buf = connection.recv(1024)  
            ins = create_message(unit)
            data = ins.SerializeToString()
            connection.send(len(data))
            connection.send(data)
        except socket.timeout:  
            print 'time out'  
        connection.close()   

if __name__ == '__main__':  
    #daemon()
    create_message(u'http://qudt.org/vocab/unit#Meter')