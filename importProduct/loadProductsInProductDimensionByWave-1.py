#encoding=utf-8
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("../utils/")
import config
import openerLogined

opener = openerLogined.login(config.olapIP90,config.username,config.passwrod)

productCategoryId = raw_input("\nInput wave product category id ,Press the enter key to exit.")
print 'Get productCategoryId='+productCategoryId+', Run service zuczug.accordingWavebandLoadProductsInProductDimension.' 

data = urllib.urlencode({"SERVICE_NAME":"zuczug.accordingWavebandLoadProductsInProductDimension","_RUN_SYNC_":"Y","POOL_NAME":"pool","productCategoryId":productCategoryId})
htmlPage = opener.open(config.serviceUrl(olapIP90),data).read()
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
