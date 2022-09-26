import socket
import sys

port = int(sys.argv[1])

# Create a connection
s = socket.socket()
s.bind(('', port))
s.listen()

while True:
    new_conn = s.accept()
    print (new_conn)
    new_socket = new_conn[0]
    req = new_socket.recv(4096)
    while True:
        req_text = req.decode("ISO-8859-1")
        print(req_text)
        print(repr(req.decode("ISO-8859-1")))
        if req_text.find('\r\n\r\n'):
            break
        req = new_socket.recv(4096)
    print("Found end of line. Closing new socket")
    new_socket.close()
