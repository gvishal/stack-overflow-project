import requests,time
def download(link):
	r = requests.get(link)
	while(r.status_code == 400):
		print "I am going off to sleep :("
		time.sleep(2)
		r = requests.get(link)
	print "I am done sleeping :)"
	return r
