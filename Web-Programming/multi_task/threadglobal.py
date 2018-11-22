'''
多线程共享全局变量,
函数对全局变量进行修改，看到底对全局变量的执行指向
利用互斥锁解决资源竞争
思考mutex加锁的位置
'''
import time
import threading

g_num = 0

def test1(num):
	global g_num
	for i in range(num):
		mutex.acquire()	
		g_num += 1
		mutex.release()
	print("in test1 g_num=%d \n" % g_num)

def test2(num):
	global g_num
	for i in range(num):
		mutex.acquire()	
		g_num += 1
		mutex.release()
	print("in test2 g_num=%d \n" % g_num)

mutex = threading.Lock()

def main():
	t1 = threading.Thread(target=test1, args=(1000000,))
	t2 = threading.Thread(target=test2, args=(1000000,))

	t1.start()
	t2.start()
	time.sleep(1)

	print('----in main thread g_num= %d' % g_num)

if __name__ == "__main__":
	main()