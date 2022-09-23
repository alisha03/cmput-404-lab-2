import socket
from multiprocessing import Pool

#define address, buffer_size
HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024
payload = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'


def make_connection(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR) 

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(make_connection, address * 4)

if __name__ == "__main__":
    main()