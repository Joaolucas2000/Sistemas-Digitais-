
import socket

'''Mesmas configs do server'''
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) ##IP

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #especificações do socket
client.connect(ADDR)

def send(msg):
    
    message = msg.encode(FORMAT) #fazer o encoder para o formato especificado
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)#tamanho da mensagem
    send_length += b' ' * (HEADER - len(send_length)) #completando ate o tamanho total de 64bytes
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))#imprime a mensagem de confirmação do server



send("Hello World!")

input()

send("Hello Everyone!")

msg1 = input()
send(msg1) #enviando mensagem do terminal 

send(DISCONNECT_MESSAGE)
