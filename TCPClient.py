from socket import *
serverIP = '10.7.33.18'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

f = open(r'client_sent.mp4', 'rb')  # file in same folder as .py file

data = f.read(1024)
while data:
    clientSocket.send(data)
    print('Sent ', repr(data))
    data = f.read(1024)

f.close()
print("\nfile transfer successful.")
clientSocket.close()
print("\nConnection Closed.")
