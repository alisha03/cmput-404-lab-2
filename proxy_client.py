import socket

#define address, buffer_size
HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024
payload = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

address = ('127.0.0.1', 8001)

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
    make_connection(address)

if __name__ == "__main__":
    main()