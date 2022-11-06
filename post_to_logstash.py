import socket
import json
import sys

HOST = '0.0.0.0'
PORT = 5044

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

msg = {'@message': 'python test message', '@tags': ['python', 'test']}

sock.send(str(json.dumps(msg) ).encode('utf-8') )

sock.close()
sys.exit(0)
