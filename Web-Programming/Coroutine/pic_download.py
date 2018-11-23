import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)
	img_content = req.read()
	with open(img_name, 'wb') as f:
		f.write(img_content)


def main():
	gevent.joinall([
		gevent.spawn(downloader, '1.jpg', "http://mm.chinasareview.com/wp-content/uploads/2017a/05/04/06.jpg"),
		gevent.spawn(downloader, '2.jpg', "http://mm.chinasareview.com/wp-content/uploads/2017a/05/19/limg.jpg")
		])

if __name__ == "__main__":
	main()



