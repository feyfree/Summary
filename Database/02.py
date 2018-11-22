from pymysql import connect

def main():
	conn = connect(host='localhost', port=3306, user='root', password='password', database='jing_dong', charset='utf8')
	cursor = conn.cursor()
	for i in range(100000):
		cursor.execute("insert into test_index values('ha-%d')" % i)
	conn.commit()

if __name__ == "__main__":
	main()
