import socket
from params import PORT, VALID_FILES_ON_SERVER


from _thread import *
import threading

server_lock = threading.Lock()

#   Section 3: Multi Thread
def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Connection closed!')
            server_lock.release()
            break
        if data not in VALID_FILES_ON_SERVER:
            c.send(f'Can not find {data} on server! Please chose your file in {VALID_FILES_ON_SERVER}')
        with open(data, 'r') as f:
            c.send(f.read().encode())
    c.close()


def server():
    host = socket.gethostname()
    port = PORT

    server_socket = socket.socket()
    server_socket.bind((host, port))

    print("Server is listening...")

    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()
        server_lock.acquire()
        print("Connection from: " + str(address))

        #   Section 1: Greeting
        conn.send('Welcome to my server'.encode())

        #   Section 2: Sending data
        with open('data.txt', 'r') as f:
            data = f.read()
            conn.send(data.encode())
        
        start_new_thread(threaded, (conn,))
        
    conn.close()


if __name__ == '__main__':
    server()
