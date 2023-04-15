
import socket #Import do modulo socket
TCP_IP = "127.0.0.1"    # Ip do servidor
FILE_PORT = 5005        #Porta Usada
DATA_PORT = 5006        #Porta de dados
timeout = 3             #Tempo limite
buf = 1024              #Buffer

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Começar o socket
sock_f.bind((TCP_IP, FILE_PORT))    #Configs do sockets
sock_f.listen(1)    #Solicitação de conexões

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Inicia socket
sock_d.bind((TCP_IP, DATA_PORT))  #Criação do servidor
sock_d.listen(1)    #Lendo conexoes
while True:
    conn, addr = sock_f.accept()    #conn e adress
    data = conn.recv(buf)           #Nome do arquivo
    if data:    #If True
        print("File name:", data)   #Imprime o nome do arquivo
        file_name = data.strip()    #Remove espaços
    f = open(file_name, 'a') #Instancia o arquivo
    conn, addr = sock_d.accept() #Colocando a conn e do address ao aceitar a conexão com o client
    while True:
        data = conn.recv(buf) #Armazena os dados 
        if not data:          #Se vazio da um break
            break
        f.write(data)         #Salva os dados em um arquivo
    print("%s Finish!", file_name) #Imprime a finalização da escrita do arquivo
    f.close()                 #Fecha arquivo
