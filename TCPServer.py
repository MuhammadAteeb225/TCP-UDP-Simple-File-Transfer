# code by Muhammad Ateeb
from socket import *
serverPort = 12000
serverIP = '10.7.33.18'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    with open(r'server_received.mp4', 'wb') as f:
        while True:
            data = connectionSocket.recv(1024)
            if not data:
                break
            print('received= ', repr(data))
            # write data to a file
            f.write(data)
    print("File Received")
    connectionSocket.close()
