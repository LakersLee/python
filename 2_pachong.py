import ssl
ssl._create_default_https_context = ssl._create_unverified_context	

from urllib.request import urlopen
from urllib.error import URLError,HTTPError

def download(url,retry_times=2):
	'''
		返回HTML字符串
	'''
	try:
		html = urlopen(url).read().decode()
	except HTTPError as e:
		print('[HTTPError]: %s' % url)
		html = None
		#取出报错状态码hasattr(e,'code'),如果有报错，尝试重新下载
		if retry_times > 0:
			print('正在尝试重新下载第%d次...' % (3-retry_times))
			if hasattr(e,'code') and 500 <= e.code <= 600:
				#print(type(e.code))
				html = download(url,(retry_times-1))
	except URLError as e:
		html = None
		print('[URLError]: %s' % url)
	return html

def main():
	#url = 'https://www.baidu.com'
	#url = 'https://www.xjioahsuabsuuag.com'
	#url = 'https://www.youtube.com'
	url = 'https://httpstat.us/500'
	#url = 'https://github.com/LakersLee'
	rt = download(url)
	print(rt)

if __name__ == '__main__':
	main()



