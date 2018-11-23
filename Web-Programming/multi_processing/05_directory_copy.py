import os
import multiprocessing 


def copy_file(q, file_name, folder_name, new_folder_name):
	'''
	完成文件的复制
	'''
	old_f = open(folder_name+'/'+file_name, 'rb')
	content = old_f.read()
	old_f.close()

	new_f = open(new_folder_name+'/'+file_name, 'wb')
	new_f.write(content)
	new_f.close()

	q.put(file_name)


def main():
	# 获取copy的文件夹的名字
	folder_name = input("please enter your folder name：")
	# 创建新的文件夹
	try:
		new_folder_name = folder_name + '[copy]'
		os.mkdir(new_folder_name) 
	except:
		pass
	# 获取要考呗的文件名字
	file_names = os.listdir(folder_name)
	# print(file_names)
	# 创建进程池
	
	po = multiprocessing.Pool(5)
	q = multiprocessing.Manager().Queue()

	for file_name in file_names:
		po.apply_async(copy_file, args=(q, file_name, folder_name, new_folder_name))
	
	po.close()
	f_num = len(file_names)
	copy_num = 0
	while True:
		f_name = q.get()
		# print("已经完成copy：%s" % f_name)
		copy_num += 1
		print("\r完成进度：%.2f%%" % (copy_num*100/f_num), end='')
		if copy_num >= f_num:
			break
	print('\n')
	po.join()


if __name__ == "__main__":
	main()