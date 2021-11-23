#SERVER

import socket
import sys
import time


IP = '0.0.0.0'
PORT = 33333
SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen()
print(f'starting up on {IP}, port {PORT}')



def upload():
	file_name = client_socket.recv(SIZE).decode().split('/')[-1]
	print(f"[+] [received] upload, file name: {file_name}")

	with open(f'/home/leonhard/cyber/{file_name}', 'wb+') as f:
		data = client_socket.recv(SIZE)

		while data:
			f.write(data)
			data = client_socket.recv(SIZE)
	print("[!] Done")
	return
	
if __name__ =="__main__":
	while True:
		client_socket, address = s.accept()               
		print(f'[!] {address} is connected')	
		upload()



