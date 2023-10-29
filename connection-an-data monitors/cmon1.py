import socket
import os
import signal
import sys
from collections import Counter

connection_counts = Counter()

log_file = "connected_ips.txt"

def signal_handler(signal, frame):
    top_ips = connection_counts.most_common(10)

    os.system("clear")
    print("\033[1m\033[97mIP addresses with the most connections\033[93m:\033[0m")
    for ip, count in top_ips:
        print(f"\033[97mIP address: \033[93m{ip} \033[97m(Count: \033[92m{count}\033[97m)\033[0m")

    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 22 # replace this with desired port number skiddo
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"\033[1m\033[97mListening on port \033[93m{port}\033[97m . . .\033[0m")

    while True:
        client_socket, addr = server_socket.accept()
        ip = addr[0]
        print(f"\033[92mNew connection from \033[97m{ip}\033[0m")

        connection_counts[ip] += 1

        with open(log_file, "a") as f:
            f.write(f"Connected IP: {ip}\n")

        client_socket.close()

if name == "main":
    main()