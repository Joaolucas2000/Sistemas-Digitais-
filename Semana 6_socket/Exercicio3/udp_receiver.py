import socket #Import modulo socket
import select #Import modulo select

UDP_IP = 127.0.0.1 #Ip do servidor
IN_PORT = 5005 # porta servidor
timeout = 3 #Tempo maximo
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Instancia Socket
sock.bind((UDP_IP, IN_PORT)) #Cria o servidor

while True:
    data, addr = sock.recvfrom(1024) #tamanho
    if data:
        print (File name:, data)
        file_name = data.strip()
    f = open(file_name, 'wb') #Open arquivo - escrita binario
    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024) #Tamanho
            f.write(data) #escrever dados
        else:
            print(%s Finish! % file_name) #Mostra a finalização
            f.close() #Fecha o arquivo
            break 
