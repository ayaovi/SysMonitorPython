import socket
#import psutil
#psutil.pids()
import os

HOST, PORT = '', 2222	# listening on port 2222 :)

#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server_socket.bind((HOST, PORT))
#server_socket.listen(1)

print 'Listening on port %s ...' % PORT
#while True:
#    client_connection, client_address = server_socket.accept()
#    request = client_connection.recv(1024)
#    print request

#    http_response = """\
#HTTP/1.1 200 OK

#Hello, World!
#"""
#    client_connection.sendall(http_response)
#    client_connection.close()

#os.system("top > process.dat")
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids:
    try:
        print open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
    except IOError: # proc has already terminated
        continue

#for proc in psutil.process_iter():
#    try:
#        pinfo = proc.as_dict(attrs=['pid', 'name'])
#    except psutil.NoSuchProcess:
#        pass
#    else:
#        print(pinfo)

print("Recorded processes")
