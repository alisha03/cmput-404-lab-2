import socket, time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

# handle requests and sends data back to client
def handle_request(addr, conn, google_socket):
    # send client request to google
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending recieved data {send_full_data} to google")
    time.sleep(0.5)
    google_socket.sendall(send_full_data)
    google_socket.shutdown(socket.SHUT_WR)

    #send received data back to client
    google_data = google_socket.recv(BUFFER_SIZE)
    conn.send(google_data)

def main():

    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as google_socket:
                remote_ip = get_remote_ip(host)
                google_socket.connect((remote_ip, port))
                
                p = Process(target=handle_request, args=(addr, conn, google_socket))
                p.daemon = True
                p.start()
                print("Started process", p)

            conn.close()

if __name__ == "__main__":
    main()