class Goods:
	@property
	def size(self):
		return 100

obj = Goods()
ret = obj.size
print(ret)