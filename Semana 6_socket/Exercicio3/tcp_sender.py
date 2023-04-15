
import socket #Importamos modulo socket
import sys #Importamos modulo sys para trabalhar com arquivos

TCP_IP = "127.0.0.1"    #IP do servidor
FILE_PORT = 5005        #Porta de arquivo
DATA_PORT = 5006        #Porta de dados
buf = 1024              #Buffer
file_name = input("nome: ")#Pega nome do arquivo pelo usuario

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #inicialização(instancia) do socket
    sock.connect((TCP_IP, FILE_PORT)) #Conexao socket-localhost
    sock.send(file_name)              #Manda o nome do arquivo
    sock.close() #Fecha o socket


    print("Sending %s ...", file_name) #printa status


    f = open(file_name, "rb") #Open arquvio, leitura-binario
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Inicialização do socket
    sock.connect((TCP_IP, DATA_PORT))   #Conexao com o host
    data = f.read()                     #Escreve os dados no arquivo
    sock.send(data)                     #Envia o arquivo
finally:
    sock.close()    #Fecha conexão
    f.close()       #Fecha arquivo
