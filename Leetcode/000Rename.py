import os

def judge(s):
	m = 0
	for i in s:
		if i !='_' and i !='R':
			m += 1
		else:
			break
	return m

def main():
	file_list = os.listdir()
	for i in file_list:
		remain = 3-judge(i)
		os.rename(i, '0'*remain+i)
	
if __name__ == "__main__":
	main()