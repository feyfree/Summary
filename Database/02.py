from pymysql import connect

conn = connect(host='localhost', port=3306, user='root', password='wudishuno1', database='jing_dong', charset='utf8')
cursor = conn.cursor()

cursor.excute()