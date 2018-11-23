'''
生成器，是一种迭代器

'''

def create_num(all_num):
	a, b =0, 1
	current_num = 0
	while current_num < all_num:
		ret = yield a		#send的值传递到ret里面
		print('----ret>>>>>', ret)
		a, b = b, a+b
		current_num += 1
	return "---ok-----"

a = create_num(10)

ret = next(a)
print(ret)

ret = a.send('haha') 
print(ret)

ret = next(a)
print(ret)


ret = next(a)
print(ret)


# while True:
# 	try:
# 		ret = next(a)
# 		print(ret)
# 	except Exception as ret:
# 		print(ret.value)
# 		break
