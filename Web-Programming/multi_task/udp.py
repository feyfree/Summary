'''
发送和接受两个线程
'''

import time
import threading
import socket

def recv_msg(udp_socket):
	while True:
		recv_data = udp_socket.recvfrom(1024)
		print(recv_data.decode('utf-8'))

def send_msg(udp_socket, dest_ip, dest_port):
	while True:
		send_data = input("please enter your data:")
		udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udp_socket.bind(("", 6677))

	dest_ip = input("ip address:")
	dest_port = int(input('port:'))

	t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
	t2 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

	t1.start()
	t2.start()


if __name__ == "__main__":
	main()