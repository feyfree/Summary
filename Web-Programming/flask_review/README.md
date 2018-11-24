# Flask Review

#### 1.如何启动应用

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

#### 2.web 开发服务器

```python
export FLASK_APP = application.py
export FLASK_DEBUG = True
```

***服务器启动后便开始轮询，处理请求***

#### 3.动态路由

```python
@app.route
```

#### 4.请求响应循环，上下文变量

多个线程同时处理不同客户端发送的不同请求时候，每个线程看到的request对象必然不同， flask使用上下文让特定的变量在一个线程中全局访问，在此同时却不会干扰其他线程说    

| 变量名         | 上下文   | 说明                        |
|:----------- |:-----:| -------------------------:|
| current_app | 应用上下文 | 当前应用的应用实例                 |
| g           | 应用上下文 | 处理请求用作临时存储的对象，每次请求会重设这个变量 |
| request     | 请求上下文 | 请求对象，封装了客户端发出的HTTP的请求中的内容 |
| session     | 请求上下文 | 用户会话，值为一个字典，存储            |

#### 5.


