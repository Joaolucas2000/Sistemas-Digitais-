import socket #Import modulo socket
import time #Import modulo time
import sys #Import modulo sys

UDP_IP = 127.0.0.1 #IP servidor
UDP_PORT = 5005 #Porta servidor
buf = 1024 #Tamanho buffer
file_name = sys.argv[1] #Nome Arquivo

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#config do socket
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #Sender 
print (Sending %s ... % file_name) #printa que esta enviando

f = open(file_name, r) #Abre arquivo, read
data = f.read(buf)#read com tamanho buf

while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf) #envio do buffer
        time.sleep(0.02) #tempo esperando 

sock.close() #Fecha conexao
f.close() #Fecha arquivo 
