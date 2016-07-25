#encoding=utf-8
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("../utils/")
import config
import openerLogined

opener = openerLogined.login(config.loginUrl(config.erpIP80),config.username,config.password)

print("Run service importAllProductPicturesFromProductContentFact.")
data = urllib.urlencode({"SERVICE_NAME":"importAllProductPicturesFromProductContentFact","_RUN_SYNC_":"Y","POOL_NAME":"pool"})
htmlPage = opener.open(config.serviceUrl(config.erpIP80),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find("div",class_="screenlet-body")
if "success" in div.prettify():
	print 'Result: Success.'
else:
	for i in div.form.findAll("td"):
		if i.string == None or i.string == 'Save Value ?' or i.string == 'Parameter Value' or i.string == 'Parameter Name':
			continue
		print i.string	
	sys.exit(0)

print("Run service importAllCategoryPicturesFromCategoryContentFact.")
data = urllib.urlencode({"SERVICE_NAME":"importAllCategoryPicturesFromCategoryContentFact","_RUN_SYNC_":"Y","POOL_NAME":"pool"})
htmlPage = opener.open(config.serviceUrl(config.erpIP80),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find("div",class_="screenlet-body")
if "success" in div.prettify():
        print 'Result: Success.'
else:
        for i in div.form.findAll("td"):
                if i.string == None or i.string == 'Save Value ?' or i.string == 'Parameter Value' or i.string == 'Parameter Name':
                        continue
                print i.string

raw_input('\nPress the enter key to exit.')
