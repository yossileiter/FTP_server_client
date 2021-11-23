import socket
import sys
import os
import struct

#CLIENT

IP = "127.0.0.1"
PORT = 33333
SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connection():
	try:
		s.connect((IP, PORT))
		print("Connection sucessful :)")
	except:
		print("Connection unsucessful :(")
#		sys.exit()


def upload(file_name):    
	s.send(b'upload')
	s.send(file_name.encode())

	with open(file_name, 'rb') as f:
			data = f.read(SIZE)

			while data:
				s.send(data)
				data = f.read(SIZE)    
				print("[:)] successful\n")
				connection()
	return

if __name__ =="__main__":
	connection()
	upload("/home/leonhard/Downloads/IMG_5636.JPG")
