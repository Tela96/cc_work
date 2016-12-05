example_string = "abcdefghijklmnopqrstuvwxyz"

import socket
import sys


def send_to_server(my_message):
    host = "192.168.150.86"
    port = 12348                   # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(bytes(my_message, encoding="utf-8"))
    data = s.recv(1024)
    s.close()
    print('Received: ' + data.decode("utf-8"))


def encode_text(message):
    encoded = ""
    for i in (0, len(message)):
        if i <= 17:
            if example_string[i] in message:
                encoded += example_string[i + 9]
        elif i > 17:
            valami = 26 - i
            igen = 9 - valami
            encoded += example_string[igen]
    return encoded

print(encode_text("aaa"))
send_to_server('''
░░░░░░░░▄▄▄▀▀▀▄▄███▄
░░░░░▄▀▀░░░░░░░▐░▀██▌
░░░▄▀░░░░▄▄███░▌▀▀░▀█
░░▄█░░▄▀▀▒▒▒▒▒▄▐░░░░█▌
░▐█▀▄▀▄▄▄▄▀▀▀▀▌░░░░░▐█▄
░▌▄▄▀▀░░░░░░░░▌░░░░▄███████▄
░░░░░░░░░░░░░▐░░░░▐███████████▄
░░░░░░░░░░░░░▐░░░░▐█████████████▄
░░░░░░░░░░░░░░▀▄░░░▐██████████████▄
''')
