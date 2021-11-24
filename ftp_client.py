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


def upload(file_name):
	print("srart uploading")
	s.send(file_name.encode())
	with open(file_name, 'rb') as f:

		while True:
			data = f.read(SIZE)
			s.send(data)
			
			if not data:
				s.close()
			
				print("break")
				break
		   
	print("😎 successful\n")
	func_selector()			
	return


def func_selector():
	print("\n\nWelcome to the FTP client")
	print("\n\nChoose one of the following functions:\nUploading files:   upload\nDownloading files: download \nExit:              exit\n")
	while True:
		sleep(1)
		print('Enter a command')
		command = input()
	
		#if command == 'list':
		#	list_files()

		if command == 'exit':
			exit()
			break

		elif command == 'upload':
			s.send(b'upload')
			print("Enter file path")
			path = input()
			upload(path)

		elif command == 'download':	
			print("Enter file path")
			path = input()
			download(path)
		else:
			print('Command not found; please try again')



if __name__ =="__main__":
	connect()
	func_selector()
	#connection()
	#upload("/home/leonhard/Downloads/IMG_5636.JPG")
