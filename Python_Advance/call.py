class Fib():
	def __init__(self):
		pass

	def __call__(self, num):
		a = 0
		b = 1
		for i in range(num):
			yield b
			a, b = b, a+b

	def __str__(self):
		pass


f = Fib()
for i in f(10):
	print(i)
