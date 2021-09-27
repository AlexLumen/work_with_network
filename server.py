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

        for status in HTTPStatus:
            if f"status={status.value}" in data.split()[1]:
                status_value = status.value
                status_phrase = status.phrase
                break
            else:
                status_value = HTTPStatus.OK
                status_phrase = HTTPStatus(HTTPStatus.OK).phrase

        data = data.split()
        conn.send(f"{data[2]} {status.value} {status.phrase}"
                  f"\nContent-Type: text/html; charset=utf-8\n"
                  f"\nRequest Method: {data[0]}"
                  f"\nRequest Source: ({HOST},{PORT})"
                  f"\nResponse Status: {status.value} {status.phrase}"
                  f"\n{data[4:]}".encode("utf-8"))
