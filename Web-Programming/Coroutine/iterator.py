from collections import Iterable

'''
数据类型是否可以迭代
for 使用。 类型内置有iter方法， iter方法返回对象的引用(有iter和next)(即迭代器)



'''
class Myclassmate():
	def __init__(self):
		self.names = list()
		self.current_num = 0

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		return self

	def __next__(self):
		if self.current_num < len(self.names):
			ret = self.names[self.current_num]
			self.current_num += 1
			return ret
		else:
			raise StopIteration

c = Myclassmate()
c.add('li')
c.add('zhao')
c.add('wang')
for name in c:
	print(name)
