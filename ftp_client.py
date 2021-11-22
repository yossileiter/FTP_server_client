import socket
import sys
import os
import struct


# Initialise socket stuff
TCP_IP = "127.0.0.1" # Only a local server
TCP_PORT = 33333 # Just a random choice
BUFFER_SIZE = 1024 # Standard chioce
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def conn():
	#print('connecting to %s port %s' % server_address)
	#s.connect((TCP_IP, TCP_PORT))
 	# Connect to the server
    print("Sending server request...")
    try:
        s.connect((TCP_IP, TCP_PORT))
        print("Connection sucessful")
    except:
        print("Connection unsucessful. Make sure the server is online.")

conn()
