import socket

HOST = "127.0.0.1"
PORT = 11862

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT}")
    s.connect((HOST, PORT))

    while True:
        data_to_send = s.recv(1024)
        print(data_to_send.decode("utf-8"))
        #s.send(input('Send status').encode("utf-8"))
