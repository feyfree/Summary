'''
并行：真的多任务
并发：假的多任务
使用threading中的类Thread
线程的运行是没有顺序的
'''
import threading
import time

def test1():
	for i in range(5):
		print('test1-----')
		time.sleep(1)

def test2():
	for i in range(5):
		print('test2-----')
		time.sleep(1)

def main():
	t1 = threading.Thread(target=test1)
	t2 = threading.Thread(target=test2)

	t1.start()
	t2.start()

	while True:
		print(threading.enumerate())
		if len(threading.enumerate()) <= 1:
			break
		time.sleep(1)



if __name__ == "__main__":
	main()