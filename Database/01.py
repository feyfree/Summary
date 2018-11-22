from pymysql import *

class JD(object):
	def __init__(self):
		self.conn = connect(host='localhost', port=3306, user='root', password='password', database='jing_dong', charset='utf8')
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.cursor.close()
		self.conn.close()

	def execute_sql(self,sql):
		self.cursor.execute(sql)
		for temp in self.cursor.fetchall():
			print(temp)

	@staticmethod
	def print_menu():
		print('----京东----')
		print('1:所有商品')
		print('2:所有商品分类')
		print('3:所有商品品牌分类')
		print('4:添加商品品牌分类')
		print('5:根据名字查询商品')


		return input('输入序号：')

	def add_suppliers(self):
		item = input('请输入新的名字')
		sql = """ insert into suppliers (name) values ('%s')""" % item 
		self.cursor.execute(sql)
		self.conn.commit()

	def show_all_items(self):
		sql = 'select * from goods'
		self.execute_sql(sql)

	def show_catas(self):
		sql = 'select name from goods_catas'
		self.execute_sql(sql)

	def show_suppliers(self):
		sql = 'select name from suppliers'
		self.execute_sql(sql)

	def get_info_by_name(self):
		find_name = input("请输入商品名字：")
		# sql = "select * from suppliers where name='%s'" % find_name
		# print('-------%s><-----' % sql)
		sql = "select * from suppliers where name=%s"
		self.cursor.execute(sql, [find_name])
		print(self.cursor.fetchall())

	def run(self):
		while True:
			num = self.print_menu()
			if num == '1':
				self.show_all_items()
			elif num == '2':
				self.show_catas()
			elif num == '3':
				self.show_suppliers()
			elif num == '4':
				self.add_suppliers()
			elif num == '5':
				self.get_info_by_name()
			else:
				print('输入有误，重新输入')

def main():
	jd = JD()
	jd.run()

if __name__ == "__main__":
	main()