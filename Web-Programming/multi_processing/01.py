import time
import multiprocessing


'''
多进程和多线程的区别，
多进程在终端中可以看到多个进程

'''
def test1():
	while True:
		print('1------\n')
		time.sleep(1)

def test2():
	while True:
		print('2-----\n')
		time.sleep(1)

def main():
	t1 = multiprocessing.Process(target=test1)
	t2 = multiprocessing.Process(target=test2)
	t1.start()
	t2.start()


if __name__ == "__main__":
	main()