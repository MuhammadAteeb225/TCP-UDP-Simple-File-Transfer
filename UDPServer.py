from socket import *
serverPort = 25000
serverIP = "10.7.32.52"
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive")

while 1:
    message, clientAddress = serverSocket.recvfrom(1024)
    if not message:
        break
    with open(r"server.txt", "ab") as f:
        f.write(message)
