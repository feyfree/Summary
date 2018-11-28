class Province():

	country = 'China'
	
	def __init__(self, name):
		self.name = name

	@classmethod
	def class_func(cls):
		pass

	@staticmethod
	def static_func():
		pass

a = Province('jiangsu')
print(a.country)
a.__class__.country = 'USA'
c = Province('shandong')
print(c.country)
print(Province.country)

