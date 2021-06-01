#set debug=4
import sys, socket          
print(sys.path) 
from _thread import *
#print("Start")    
#sys.path+=['/home/excelvrn/Pyth/django-main']
#sys.path+=['/home/excelvrn/Pyth/asgiref-main']
#print(sys.path) 


debug = 4


sockettime = 30
#adr = ('80.82.63.117', 8990)
#adr = ("192.168.1.1", 8000)
adr = ("", 8000)

listenvar = 100

htmlsite = b'<html><head></head><body><div>asdf</div></body></html>'

def pr(x):
    print("\tX:\t", x)
    pass


def create():
    socket.setdefaulttimeout(sockettime)
    #adr = ("80.82.63.117", 80)
    adr = ("192.168.1.1", 80)
    serv_sock = socket.create_connection(adr)
    
    print(serv_sock.accept())
    
    print(serv_sock, "\n")
    as_se_sock = serv_sock.accept()
    print(as_se_sock)
    print(serv_sock.close())
    print("END")
    pass
def create2():
    #adr = ('192.168.1.1', 80)
    socktype = socket.SOCK_STREAM
    
    #socket
    #serv_sock = socket.socket(socket.AF_INET, socktype)
    serv_sock = socket.socket()
    print(serv_sock)
    #bind
    serv_sock.bind(('', 80))
    serv_sock.listen(1)
    #print()
    

    pass
def create3():
    sock = socket.socket()
    socket.setdefaulttimeout(sockettime)
    
    print(sock)
    pr(1)
    sock.bind(adr)
    pr(2)
    sock.listen(listenvar)
    pr(3)
    conn, addr = sock.accept()
    print('conn, addr:\t',conn, addr)
    pr(4)
    print('connected:', addr)

    while True:
        print( 'sock.getpeername():\t', sock.getsockname())
        data = conn.recv(1024)
        pr(5)
        print(data)
        sdata = b'GET / HTTP/1.1\r\nUser-Agent: ExcelvrnJob\r\n\r\n'
        conn.send(htmlsite)
        if not data:
            break


   
    pr(5)
    print(conn)
    print(sock)     
    while 1:
        pass
    conn.close()
    pass
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()	
    pass	
def create4():
	ServerSocket = socket.socket()
	host = ''
	port = 8000
	ThreadCount = 0
	try:
		ServerSocket.bind((host, port))
	except socket.error as e:
		print(str(e))

	print('Waitiing for a Connection..')
	ServerSocket.listen(5)
	while True:
		Client, address = ServerSocket.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread(threaded_client, (Client, ))
		ThreadCount += 1
		print('Thread Number: ' + str(ThreadCount))
	ServerSocket.close()
	pass
	
def name():
    print(socket.gethostname())
    
    #print( socket.gethostbyaddr('192.168.1.33'))
    print( socket.gethostbyaddr('80.82.63.117'))
    print( socket.sethostname(name))
    pass
if debug == 0:
    create()
elif debug == 1:
    name()
elif debug == 2:
    create2()
elif debug == 3:
    create3()
elif debug == 4:
    create4()
    
