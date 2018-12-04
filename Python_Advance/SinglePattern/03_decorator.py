from functools import wraps

def singleton(cls):
	instances = {}
	@wraps(cls)
	def getinstance(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return getinstance

@singleton
class MyClass():
	a = 1

foo1 = MyClass()
foo2 = MyClass()

print(foo1 is foo2)