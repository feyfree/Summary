import multiprocessing

def download_from_web(q):
	#模拟下载数据
	data = [11,22,33,44]
	for temp in data:
		q.put(temp)
	print("下载器下载完了数据存入队列")

def analysis_data(q):
	waiting = list()
	while True:
		data = q.get()
		waiting.append(data)
		if q.empty():
			break
	print(waiting)

def main():
	q = multiprocessing.Queue()
	p1 = multiprocessing.Process(target=download_from_web, args=(q,))
	p2 = multiprocessing.Process(target=analysis_data,args=(q,))
	p1.start()
	p2.start()

if __name__ == "__main__":
	main()
