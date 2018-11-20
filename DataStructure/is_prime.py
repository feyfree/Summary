'''
知识点；迭代器，生成器，匿名函数，函数式编程
'''
def _odd_iter():
	'''
	奇数生成器
	'''
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	'''
	判断是否能整除n
	'''
	return lambda x : x%n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

a = primes()
print(next(a))