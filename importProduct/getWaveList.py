#encoding=utf-8
import urllib
import sys
from bs4 import BeautifulSoup
sys.path.append("../utils/")
import openerLogined
import config

opener = openerLogined.login(config.loginUrl(config.megatronIP80),config.username,config.password)

data = urllib.urlencode({"group":"org.ofbiz","sqlCommand":"SELECT PRODUCT_CATEGORY_ID, CATEGORY_NAME FROM PRODUCT_CATEGORY WHERE PRODUCT_CATEGORY_TYPE_ID ='WAVE'","rowLimit":"2000"})
htmlPage = opener.open(config.entityUrl(config.megatronIP80),data).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
table = soup.find("table",class_="basic-table hover-bar")
for i in table.contents[2:]:
	if str(i) == None or '' == str(i).strip():
		continue
	print str(i).replace('<tr class="alternate-row">',"").replace("<tr>","").replace("</tr>","").replace("\n"," ").replace("<td>","").replace("</td>","").strip()
raw_input('\nPress enter key to quit.')
