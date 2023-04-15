#!/usr/bin/python3

import socket 
import sys


# criando um servidor TCP/IP para socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost',30001)
sock.bind(server_address)

# Start the server to listen incoming connections
sock.listen(1)

while True:
	# Esperando por uma conexão
	print("Esperando por nova conexao!!")
	connection, client_address = sock.accept()
	
	try:
		while True:
			data = connection.recv(100)
			print('recebido: {!r}'.format(data))
			
			if data:
				print('reenviando mensagem para o cliente: ', client_address)
				connection.sendall(data)
			else:
				print('não foi recebida nenhum dado de: ', client_address)
				break
	finally:
		# Encerrando e limpando os dados da conexão
		connection.close()

