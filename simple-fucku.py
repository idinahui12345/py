import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("87.68.221.248",80))
        s.sendall(b"HELLO FRIENDS!")
