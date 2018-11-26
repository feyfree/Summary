'''
re模块的使用
re.match(正则表达式， 需要处理的字符串)
所有大写都是小写的相反

'''
import re

print(re.match(r"hello", "hello, world").group())
print(re.match(r"hello.", "hello*, worlds").group()) #.是什么都可以除去‘\n’
print(re.match(r"速度与激情\d{1,2}", "速度与激情21").group())

