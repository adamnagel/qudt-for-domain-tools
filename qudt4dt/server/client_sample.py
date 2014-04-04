import sys sys.path.append("../../")
import socket  
import time 
import qudt4dt
def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.connect(('localhost', 3031))  
    time.sleep(2)  
    unit = u'http://qudt.org/vocab/unit#Meter'
    sock.send(unit)
    
    back = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    back.bind(('localhost', 3032))  
    back.listen(10)  
    length = ''
    connection,address = back.accept() 
    length = connection.recv(1024)
    #print length
    ins = qudt4dt.qudt_pb2.Unit()
    ins.ParseFromString(length)
    print ins.__dict__
    back.close()
    sock.close() 
    
    
if __name__ == '__main__':  
    client()