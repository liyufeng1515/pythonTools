#encoding=utf-8
import urllib2
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import cookielib
from bs4 import BeautifulSoup

def login(loginUrl,username,password):
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
	data = urllib.urlencode({"USERNAME":username,"PASSWORD":password})
	htmlPage = opener.open(loginUrl,data).read()
	soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
	div = soup.find("div",class_="content-messages errorMessage")
	if None == div:
		print '\nLogin success.\n'
		return opener
	else:
		for i in div.contents:
			if '' == i.string.strip():
				continue
			print i.string.strip()
		raw_input('\nLogin failed. Press enter key to quit.\n')
		sys.exit(0)
    except Exception,e:
        print str(e)
