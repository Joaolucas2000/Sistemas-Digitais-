import socket 
import threading

HEADER = 64 #Tamando em bytes do header
PORT = 5050 #Porta aser usada
SERVER = socket.gethostbyname(socket.gethostname()) #Pega o IP
print(SERVER)
ADDR = (SERVER, PORT) #Uma tupla que usaremos para ligar o server
FORMAT = 'utf-8' #Formato de encoder
DISCONNECT_MESSAGE = "!DISCONNECT" #Mensagem que mandamos ao servidor que desconectamos

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Parametros do server
server.bind(ADDR) #Criação do server

def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #tamanho da mensagem e formato de encoder
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE: #Se recebermos uma mensagem de desconectar, pularemos para conn.close
                connected = False 

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT)) #envia a confirmação da msg recebida

    conn.close()
        

def start():
    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #Cria a thread para ficar lendo o servidor em paralelo
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")

start() # Aqui chamamos a função para iniciar o site
