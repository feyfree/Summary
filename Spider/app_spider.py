import requests
import json
import csv

def get_content(n):
	url = "http://zhishu.analysys.cn/public/qianfan/topRank/listTopRank?page={}&pageSize=200&cateId=&tradeId=".format(n)
	response = requests.get(url)
	res_content = json.loads(response.content).get('datas').get('list')
	out = open('app_csv.csv','a', newline='')
	for i in res_content:
		obj = list(i.values())
		csv_write = csv.writer(out,dialect='excel')
		csv_write.writerow(obj)
	out.close()
	print("page " + str(n) + " finished")

def get_title():
	url = "http://zhishu.analysys.cn/public/qianfan/topRank/listTopRank?page={}&pageSize=200&cateId=&tradeId=".format(1)
	response = requests.get(url)
	res_content = json.loads(response.content).get('datas').get('list')
	obj = list(res_content[0].keys())
	out = open('app_csv.csv','a', newline='')
	csv_write = csv.writer(out,dialect='excel')
	csv_write.writerow(obj)
	out.close()

if __name__ == "__main__":
	get_title()
	for i in range(1, 11):
		get_content(i)
