#encoding=utf-8
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("../utils/")
import config
import openerLogined

opener = openerLogined.login(config.loginUrl(config.olapIP90),config.username,config.password)
#clear entity
data = urllib.urlencode({"group":"org.ofbiz.olap","sqlCommand":"TRUNCATE TABLE PRODUCT_CONTENT_FACT","rowLimit":"200"})
htmlPage = opener.open(config.entityUrl(config.olapIP90),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find('div',class_='screenlet-body')
if "Affected 0 rows." in div.contents[0]:
	print 'clear table ProductContentFact succuss.'
else:
	print div.contents[0]
	sys.exit(0)

data = urllib.urlencode({"group":"org.ofbiz.olap","sqlCommand":"TRUNCATE TABLE CATEGORY_MEMBER_FACT","rowLimit":"200"})
htmlPage = opener.open(config.entityUrl(config.olapIP90),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find('div',class_='screenlet-body')
if "Affected 0 rows." in div.contents[0]:
        print 'clear table CategoryMemberFact succuss.'
else:
        print div.contents[0]
	sys.exit(0)

data = urllib.urlencode({"group":"org.ofbiz.olap","sqlCommand":"TRUNCATE TABLE CATEGORY_CONTENT_FACT","rowLimit":"200"})
htmlPage = opener.open(config.entityUrl(config.olapIP90),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find('div',class_='screenlet-body')
if "Affected 0 rows." in div.contents[0]:
        print 'clear table CategoryContentFact succuss.'
else:
        print div.contents[0]
	sys.exit(0)

productCategoryId = raw_input("\nInput wave product category id ,Press the enter key to exit.\n")
print 'Get productCategoryId='+productCategoryId+', Run service loadAllImageData.'

data = urllib.urlencode({"SERVICE_NAME":"loadAllImageData","_RUN_SYNC_":"Y","POOL_NAME":"pool","productCategoryId":productCategoryId})
htmlPage = opener.open(config.serviceUrl(config.olapIP90),data).read()
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
