'''
tcp服务器
建立服务器套接字
绑定端口
设置监听
等待用户
接受请求
'''

import socket 

def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.bind(("", 7789))
	tcp_server_socket.listen(128)
	new_cli_socket, cli_addr = tcp_server_socket.accept()

	recv_data = new_cli_socket.recv(1024)
	print(recv_data.decode('utf-8'))
	new_cli_socket.close()
	tcp_server_socket.close()

if __name__ == '__main__':
	main()