import socket

HOST, PORT = '', 2080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    while True:
        conn, addr = s.accept()
        with conn:
            request_data = conn.recv(1024*8).decode()
            http_response = b"HTTP/1.1 200 OK\r\n\r\n<html>Hello Friend!</html>"
            conn.sendall(http_response)
