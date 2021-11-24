#SERVER

import socket
import sys
import time


IP = '0.0.0.0'
PORT = 33333
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen()
print(f'starting up on {IP}, port {PORT}')


def upload():
	file_name = client_socket.recv(SIZE).decode()
	file_name = file_name.split('/')[-1]
	print(f"file name is: {file_name}\n")

	with open(f'/home/leonhard/cyber/{file_name}', 'wb+') as f:
		#data = client_socket.recv(SIZE)

		while True:
			#f.write(data)
			data = client_socket.recv(SIZE)
			f.write(data)
			if not data:
				print("finishing")
				break
			#f.write(data)		
		print("😎 Done\n")
	#func_selector()
	return

def func_selector():
	command = client_socket.recv(SIZE).decode()
	print("the command is: ", command)
	if command == "upload":
		upload()
	

if __name__ =="__main__":
	while True:
		client_socket, address = s.accept()               
		print(f'[!] {address} is connected')	
		func_selector()


