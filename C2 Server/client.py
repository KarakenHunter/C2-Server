import socket

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9821))

    command = input("Enter command: ")
    sock.send(command.encode())

    result = sock.recv(4096).decode()
    print(result)

    sock.close()

client()