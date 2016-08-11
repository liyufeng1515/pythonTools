#encoding=utf-8
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("../utils/")
import config
import openerLogined

opener = openerLogined.login(config.loginUrl(config.olapIP80),config.username,config.password)

productCategoryId = raw_input('\nInput wave product category id,Press enter key to exit.\n')
print 'Get productCategoryId='+productCategoryId+',Run service BluemountainProductMove.'

data = urllib.urlencode({"SERVICE_NAME":"BluemountainProductMove","_RUN_SYNC_":"Y","POOL_NAME":"pool","way":"2","productId":productCategoryId})
htmlPage = opener.open(config.serviceUrl(config.olapIP80),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find("div",class_="screenlet-body")
if "success" in div.prettify():
    print "Result: Success."+div.get_text()[div.get_text().index("successMessage"):div.get_text().index("Clear")]
else:
	for i in div.form.findAll("td"):
		if i.string == None or i.string == 'Save Value ?' or i.string == "Parameters Value" or i.string == "Parameter Name":
			continue
		print i.string
raw_input('\nPress the enter key to exit.')
