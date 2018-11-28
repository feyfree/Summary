class Goods:
	@property
	def price(self):
		print('@property')

	@price.setter
	def price(self, value):
		print('@price.setter')

	@price.deleter
	def price(self):
		print('@price.deleter')

obj = Goods()
obj.price
obj.price = 123
