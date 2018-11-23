'''
生成器，是一种迭代器

'''

def create_num(all_num):
	a, b =0, 1
	current_num = 0
	while current_num < all_num:
		yield a
		a, b = b, a+b
		current_num += 1

a = create_num(10)

for i in a:
	print(i)
