# Flask Review--------------------------------重新熟悉一下Flask



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

没激活上下文就调用current_name会导致错误， 获取应用上下文的方法是在应用实例上调用app.app_context( ) 

flask通过上下文变量request对外开放请求对象

#### 5. 一些跳转（响应）的对比

| 函数                | 说明          |
| ----------------- | ----------- |
| render_template() | 向Jinja2返回模版 |
| url_for()         | 返回视图函数      |
| make_response( )  | 响应          |
| redirect()        | 重定向         |

#### 6. 重定向和用户会话

##### 技巧

Post / 重定向 / Get模式

用户可以把数据存储在用户会话中

#### 7. SQLAlchemy的数据库

```python
class Role(db.Model):
    # ...
    # users属性将返回与角色相关联的用户组成的列表
    users = db.relationship('User', backref='role')


class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

类Role中， backref参数向User模型中添加一个role模型，从而定义反向关系

```python
>>>admin_role = Role(name='Admin')
>>>user_john = User(name='John', role=admin_role)
>>>users = admin_role.users
>>>[<'User' John>]
```

lazy属性， lazy=“dynamic” 表示从而禁止自动执行查询

#### 8. 视图函数中操作数据库

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),             known=session.get('known', False))
```

#### 9. 数据库迁移

```python
from flask_migrate import Migrate
# ...
migrate = Migrate(app, db)
```

1. 对模型类做必要的修改

2. 执行flask db migrate命令，自动创建一个迁移脚本

3. 检查自动生成的脚本，根据对模型的实际改动进行调整

4. 把迁移脚本纳入版本控制

5. 执行flask db upgrade命令， 把迁移应用到数据库

   #### 

#### 10. 电子邮件

```python
from flask_mail import mail
mail = Mail(app)
```

```python
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject, sender=........)
    msg.body = render_template(template+'.txt', )
    msg.html = render_template(template+'.html', )    
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
        
```

#### 11. 文件架构

1. 应用包app

2. 数据库迁移脚本

3. 单元测试包

4. 虚拟环境包

5. 依赖

6. 配置

7. 应用实例（启动应用）

#### 12. 应用的配置

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get()
    #.....
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLAlCHEMY_DATABASE_URI = os.environ.get().........

class TestingConfig(Config):
    TESTING = True
    #.....
    
config = {
    'development': DevelopmentConfig
    #....
} 
```

基类Config中包含通用配置，config字典

#### 13. 应用工厂函数

应用包的构造函数

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    return app

```

#### 14. 在蓝本中实现应用功能

app/main/__init_ __ .py

```python
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
```

app/___init_ __.py

```python
def create_app(config_name):
    #...
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
```

#### 15. 应用脚本

```python
import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_process
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

#### 16. 单元测试

```python
import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_app_exist(self):
        self.assertFalse(current_app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['Testing'])
```



**flasky.py**

```python
@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
```


