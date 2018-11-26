import socket
import re
import select


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求  
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode("utf-8")
    # print(">>>"*50)
    # print(request)

    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据，给浏览器
    
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header

        response_body = html_content 

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode('utf-8') + response_body

        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response)

    # 关闭套接
    # new_socket.close()
    

def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 6100))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False) #设置为非阻塞
    # 创建epoll对象
    epl = select.epoll()
    # 将套接字对象文件描述符
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)  # 监测是否有输入
    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll() #默认阻塞，知道os监测到数据到来，通过事件通知，解阻塞
        #[(fd, event),]文件描述符，事件类型
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                #判断已经连接的客户端是否有数据传来
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
