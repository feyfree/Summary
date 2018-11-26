import socket
import re
import multiprocessing

def service_client(new_socket):
	# 为这个客户返回数据
	# 1.接受浏览器发挥的http请求
	# GET /Http
	request = new_socket.recv(1024).decode('utf-8')
	request_lines = request.splitlines()
	print(">"*20)
	print(request_lines)
	# 准备发送给浏览器的数据header
	# 准备发送给浏览器的数据body

	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	if ret:
		file_name = ret.group(1)

	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"
	with open("./html"+file_name, 'rb') as f:
		html_content = f.read()
	new_socket.send(response.encode('utf-8'))
	new_socket.send(html_content)
	new_socket.close()

def main():
	# 1.创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 2.绑定
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	tcp_server_socket.bind(("", 7890))
	# 3.设置监听
	tcp_server_socket.listen(128)
	while True:
		# 4.等待客户端响应
		new_socket, client_addr = tcp_server_socket.accept()
		# 5.为这个客户端服务
		p = multiprocessing.Process(target=service_client, args=(new_socket,))
		
	tcp_server_socket.close()

if __name__ == "__main__":
	main()