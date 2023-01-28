import socket
from params import PORT

def client():
    host = socket.gethostname()
    port = PORT

    client_socket = socket.socket()
    client_socket.connect((host, port))

    #   Section 1: Greeting
    data = client_socket.recv(1024).decode()
    print('Received from server:', data)

    #   Section 2: Sending data
    data = client_socket.recv(1024).decode()
    print('Received from server:', data)

    with open('data-client.txt', 'w') as f:
        f.write(data)

    #   Section 3: Multi Thread
    message = input(" -> ")
    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client()