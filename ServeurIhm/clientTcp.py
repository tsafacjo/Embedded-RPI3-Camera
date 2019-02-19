import socket


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1977))
s.send("p")
s.send("p")
s.close()
