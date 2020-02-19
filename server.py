import socket
import pickle
from _thread import *
from battleship import game

server = '127.0.0.1'
port = 8000
client_num = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = [game(1), game(2)]
try:
    s.bind((server, port))
except socket.error as error:
    print(error)
s.listen(2)
print("Waiting for connection...")

def create_thread(conn, client_num):
    conn.send(pickle.dumps(connections[client_num]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            connections[client_num] = data
            if client_num == 1:
                reply = connections[0]
            else:
                reply = connections[1]
            conn.sendall(pickle.dumps(reply))
        except socket.error as e:
            print(e)
            break
        
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    start_new_thread(create_thread, (conn, client_num))
    client_num += 1
