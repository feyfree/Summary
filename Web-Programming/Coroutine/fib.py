'''
xrange()和range()在python2中有区别，前者为迭代器
list, tuple

'''
class Fib():
	def __init__(self, all_num):
		self.all_num = all_num
		self.current_num = 0
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.current_num < self.all_num:
			ret = self.a
			self.a, self.b = self.b, self.a+self.b
			self.current_num += 1
			return ret
		else:
			raise StopIteration
f = Fib(10)
for num in f:
	print(num)