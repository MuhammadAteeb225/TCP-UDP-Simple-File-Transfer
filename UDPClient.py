from socket import *
import time

serverIP = "10.7.32.52"
serverPort = 25000  # port where server is listening
clientSocket = socket(AF_INET, SOCK_DGRAM)
bufferLength = 1024
filename = r"client.txt"
f = open(filename, "r")
message = f.read(bufferLength).encode()
while message:
    clientSocket.sendto(message, (serverIP, serverPort))
    time.sleep(0.02)
    message = f.read(bufferLength).encode()
f.close()
clientSocket.close()  # Close the socket
print("***File Saved***")