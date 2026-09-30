import socket
import threading

HOST="0.0.0.0"   # server 
PORT =5000        #server port number

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #ipv4 use krto    , tcp protocols
server.bind((HOST,PORT))  # server la host ani port number deto
server.listen()   #server listening mode madhe jatto 

print(f" Server started on {HOST}:{PORT}")
print("Waiting for client..")

client,address =server.accept()     # client accept krto

print(f"Client Connected: {address}")

def receive_messages():
    while True:
        try:
            message =client.recv(1024).decode()
            
            if not message:
                break
            
            print (f"\nClient : {message}")
        except:
            break
        
thread =threading.Thread(target=receive_messages)
thread.start()

while True:
    message=input("You:") 
    
    if message.lower()=="exit":
        client.send("exit".encode())
        break
    client.send(message.encode())
client.close()
server.close()
        