#CLIENT

import socket
import sys
import os
import struct
from time import sleep

IP = "127.0.0.1"
PORT = 33333
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
	s.connect((IP, PORT))
	print("\n\n✅ connection successful")
	sleep(1)

def download(file_name):
	print(f"\nDownloading {file_name}...\n")
	s.send(file_name.encode()) 

	with open(f'/home/leonhard/cyber/recv.{file_name}', 'wb+') as f:

		while True:
			data = s.recv(SIZE)
			f.write(data)
			if not data:
				s.close()
				print("File accepted")
				break
	func_selector()
	return

def upload(file_name):
	print("srart uploading")
	s.send(file_name.encode())
	with open(file_name, 'rb') as f:

		#while True:
		data = f.read()
		s.sendall(data)
	sleep(2)
	s.sendall(b"stop")
	print("😎 successful\n")



def list_files():
	print("Receiving list of files...\n")
	data = str(s.recv(SIZE).decode())
	data = data.strip("[]")
	data = data.split(", ")
	for i in data:
		i = i.strip("''")
		print(f"📂 {i}")
	
	print("\n\nThat's it...")
	func_selector()

def func_selector():
	print("\n\nWelcome to the FTP client")
	print("\n\nChoose one of the following functions:\nUploading files:   upload\nDownloading files: download \nlist of files:     list\nExit:              exit\n")
	while True:
		sleep(1)
		print('Enter a command')
		command = input()
	
		if command == 'list':
			s.send(b'list')
			list_files()

		elif command == 'exit':
			exit()
			break

		elif command == 'upload':
			s.send(b'upload')
			print("Enter file path")
			path = input()
			upload(path)

		elif command == 'download':	
			s.send(b'download')
			print("Enter file name")
			file_name = input()
			download(file_name)
		else:
			print('Command not found; please try again')



if __name__ =="__main__":
	connect()
	func_selector()

