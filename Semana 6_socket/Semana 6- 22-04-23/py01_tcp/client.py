#!/usr/bin/python3

import socket
import sys


# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dados para a conexão com o servidor
server_address = ('localhost',30001)
print('Conectando à - {}:{}'.format(*server_address))


try:
	sock.connect(server_address)	
	msg = b'Messagem enviada pelo cliente'
	tam = len(msg)
	for i in range(5):
		# Aguarda ser enviado
		inp = input("Pressione enter para continuar")

		# envio da mensagem
		print(i + 1, msg)
		sock.sendall(msg)
		
		# recebimento da mensagem
		recebido = 0
		while recebido < tam:
			data = sock.recv(100)
			recebido += len(data)
			print('{!r}'.format(data))
	
finally:
	print('finalizando a conexão')
	sock.close()
