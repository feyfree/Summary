import socket 

def service_client(new_socket):
	# 1.接收请求
	# GET / 
	request = new_socket.recv(1024)
	print(request)
	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"
	new_socket.send()

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.bind(('', 7880))
	tcp_server_socket.listen(128)
	new_socket, client_addr = tcp_server_socket.accept()
	service_client(new_socket)

if __name__ == '__main__':
	main()