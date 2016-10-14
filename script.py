import urllib.request

request = urllib.request.Request('http://placekitten.com')

try:
	response = urllib.request.urlopen(request)
	kittens = response.read()
	print(kittens[559:1000])
except URLError as e:
	print('No Kittenz. Got an error code')
	
