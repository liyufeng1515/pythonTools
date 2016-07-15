#encoding=utf-8
import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup

import sys
sys.path.append("../")
import config

def login(ip,userName,password):
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        data = urllib.urlencode({"USERNAME":userName,"PASSWORD":password})
	htmlPage = opener.open(config.loginUrl(ip),data).read()
	soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
	div = soup.find("div",class_="content-messages errorMessage")
	if None == div:
		print '\nLogin success.'
		return opener
	else:
		for i in div.contents:
			print i.string
		raw_input('\nLogin failed. Press enter key to quit.')
		sys.exit(0)
    except Exception,e:
        print str(e)
