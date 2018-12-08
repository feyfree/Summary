import socket
import StringIO
import sys
 
class WSGIServer(object):
 
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1
 
    def __init__(self, server_address):
        # 创建一个可用的socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        #socket的工作模式
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address) #绑定地址
        # Activate
        listen_socket.listen(self.request_queue_size)  #监听文件描述符
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []
 
    def set_app(self, application):
        self.application = application
 
    def serve_forever(self):   #启动WSGI server服务，不停的监听并获取socket数据。
        listen_socket = self.listen_socket
        while True:
                self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()   #处理新连接
 
    def handle_one_request(self):   #主要处理函数
        self.request_data = request_data = self.client_connection.recv(1024)
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))
 
        self.parse_request(request_data)
        env = self.get_environ()
 
        #给flask\tornado传递两个参数，environ，start_response
        result = self.application(env, self.start_response)
 
        # Construct a response and send it back to the client
        self.finish_response(result)
 
    def parse_request(self, text):    #处理socket的http协议
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line into components
        (self.request_method,  # GET
         self.path,            # /hello
         self.request_version  # HTTP/1.1
         ) = request_line.split()
 
    def get_environ(self):   #获取environ数据
        env = {}
        env['wsgi.version']      = (1, 0)
        env['wsgi.url_scheme']   = 'http'
        env['wsgi.input']        = StringIO.StringIO(self.request_data)
        env['wsgi.errors']       = sys.stderr
        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once']     = False
        env['REQUEST_METHOD']    = self.request_method    # GET
        env['PATH_INFO']         = self.path              # /hello
        env['SERVER_NAME']       = self.server_name       # localhost
        env['SERVER_PORT']       = str(self.server_port)  # 8888
        return env
 
    def start_response(self, status, response_headers, exc_info=None):   #创建回调函数.
        server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.3'),
        ]
        self.headers_set = [status, response_headers + server_headers]
 
    def finish_response(self, result):  #把application返回给WSGI的数据返回给客户端。
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            # Print formatted response data a la 'curl -v'
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()
 
SERVER_ADDRESS = (HOST, PORT) = '', 8888
 
def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)   #动态加载模块
    application = getattr(module, application)  #使用自省的模式加载application的WSGI协议入口。
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()
