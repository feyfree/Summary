class Singleton():
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance

class Foo(Singleton):
	pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)