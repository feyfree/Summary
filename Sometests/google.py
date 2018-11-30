import requests

def main():
	res = requests.get("https://www.google.com/")
	print(type(res)) # <class 'requests.models.Response'>
	print('*'*50)
	print(res.text)

if __name__ == "__main__":
	main()