import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8080

s.connect((host, port))

tm = s.recv(1024)
print("The client is waiting for connection")
s.close()