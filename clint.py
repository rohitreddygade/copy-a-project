import requests
url = "http://192.168.1.22:80" #My IP address 
fin = open('clint.py', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print(r.text)
finally:
	fin.close()

# 