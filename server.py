import socket
from http import HTTPStatus


HOST = "127.0.0.1"
PORT = 11862

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    print(f"Binding server on {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, address = s.accept()
        data = conn.recv(1024)
        data = data.decode("utf-8").strip()
        print(data)
        if 'status=404' in data:
            conn.send(f"Request Method: GET\nRequest Source: ({HOST},{PORT})"
                        f"\nResponse Status: {HTTPStatus.NOT_FOUND}  Not found"
                        f"\n{data[4:]} ".encode("utf-8"))
        else:
            conn.send(f"Request Method: GET\nRequest Source: ({HOST},{PORT})"
                      f"\nResponse Status: {HTTPStatus.OK} OK"
                      f"\n{data[4:]}".encode("utf-8"))

