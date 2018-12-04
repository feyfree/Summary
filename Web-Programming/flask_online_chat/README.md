# 基于Flask-SocketIO的在线聊天室

## 1.安装

```python
pip3 install flask-socketio
```

## 2. 功能实现

1. 建立，删除房间

2. 加入和离开房间

3. 发送信息，信息显示

## 3. 关于flask-socketio

* [flask-socketio的官方文档](https://flask-socketio.readthedocs.io/en/latest/)

Flask-SocketIO为flask应用提供了服务器和客户端低延迟的双向连接。实际上是封住了flask对WebSocket的支持， WebSocket在建立连接阶段通过Http的握手方式进行的。当连接建立后，客户端和服务器端之间就不在进行HTTP通信了，所有信息交由WebSocket托管。Flask-SocketIO使Flask应用程序可以访问客户端和服务器之间的低延迟双向通信，使客户端建立与服务器的永久连接。

* 发送信息

可以使用Ajax完成，通过Ajax使得前台定时去后台索要数据，消息频繁可以让后端直接推送数据到前台更加合适

* 应用必须提供页面上可以倒入Socket.IO库并且建立连接，比如

```python
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
</script>
```

## 4. 简单实例

```python
from flask import Flask, render_template
from flask_socketio import SocketIO 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

if __name__ == '__main__':
	socketio.run(app)
```

## 5. 应用介绍

定义全局变量

```python
channel_list = {"general": []}   # 频道列表
present_channel = {"initial": "general"}  # 当前频道
```


