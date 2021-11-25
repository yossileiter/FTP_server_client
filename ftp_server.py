#SERVER

import socket
import sys
import time
import os

IP = '0.0.0.0'
PORT = 33333
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen()
print('📞 Start listening\n')


def download():
	file_name = client_socket.recv(SIZE).decode()
	print(f"file name is: {file_name}\n")
	print("Sending...\n")
	with open(f'/home/leonhard/cyber/{file_name}', 'rb') as f:

		while True:
			data = f.read(SIZE)
			client_socket.sendall(data)
			
			if not data:
				client_socket.close()
				print("break")
				break



def upload():
	file_name = client_socket.recv(SIZE).decode()
	file_name = file_name.split('/')[-1]
	print(f"file name is: {file_name}\n")

	with open(f'/home/leonhard/cyber/{file_name}', 'wb+') as f:

		while True:
			
			data = client_socket.recv(SIZE)
			f.write(data)
			if not data:
				print("finishing")
				break

		print("😎 Done\n")
	#func_selector()
	return

def file_list():
	print("Collect data...")
	data = str(os.listdir())
	print(data)
	#client_socket.sendall(data)
	client_socket.sendall(data.encode())
	print("😎 Done\n")

def func_selector():
	command = client_socket.recv(SIZE).decode()
	print("the command is: ", command)
	if command == "upload":
		upload()
	elif command == "download":
		download()
	elif command == "list":
		file_list()
	else:
		exit()

if __name__ =="__main__":
	while True:
		client_socket, address = s.accept()               
		print(f'[!] {address} is connected')	
		func_selector()


