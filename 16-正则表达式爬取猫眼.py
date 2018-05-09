import requests
import re
import json
from requests.exceptions import RequestException
import time

headers ={
	
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}

def get_one_page(url):  # 获取页面源码
	try:
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):  #使用正则表达式进行解析（注意使用非贪婪模式）
	pattern = re.compile(r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S|re.M)
	#pattern = re.compile(r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S|re.M)
	items = re.findall(pattern,html)

	#print(items)
	for item in items:  #（对爬取的数据进行整理为字典）
		#print(item)
		yield {
			'index':item[0],
			'image':item[1],
			'title':item[2].strip(),
			'actor':item[3].strip(),
			'time':item[4].strip(),
			'score':item[5].strip() + item[6].strip()
		}
def write_to_json(content):  #数据写入
	with open('result.txt','a',encoding='utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False) + '\n')

def main(offset):

	url = 'http://maoyan.com/board/4?offset=' + str(offset)  #设置分页爬取

	html = get_one_page(url)
	#print(html)
	#parse_one_page(html)
	for item in parse_one_page(html):
		write_to_json(item)
if __name__ == '__main__':
	for i in range(10):
		main(offset=i*10)
		time.sleep(1)