#encoding=utf-8
import urllib
from bs4 import BeautifulSoup
import sys
sys.path.append("../utils/")
import openerLogined
import config

selected = None
def getSelected(selected):
	global LOGIN_URL
	global CLEAR_CACHE_URL
	if "a" == selected :
		LOGIN_URL = config.loginUrl(config.erpIP80)
		CLEAR_CACHE_URL = config.clearCacheUrl(config.erpIP80)
	elif "b" == selected:
		LOGIN_URL = config.loginHttpsUrl(config.webIP90)
		CLEAR_CACHE_URL = config.clearCacheHttpsUrl(config.webIP90)
	elif None == selected:
		selected = raw_input("\nChoose a or b. | a-->zuczughouse | b--> erp and workspace\n")
		getSelected(selected)
	else:
		selected = raw_input("["+ selected + "] is invalid. Input a or b,press enter key to exit.\n")
		getSelected(selected)

getSelected(selected)

opener = openerLogined.login(LOGIN_URL,config.username,config.password)
htmlPage = opener.open(CLEAR_CACHE_URL).read()
soup = BeautifulSoup(htmlPage,"html.parser",from_encoding="utf-8")
div = soup.find("div",id="content-messages")
if None == div :
	raw_input("Clear cache failed.Press enter key to quit.")
else:
	raw_input("Clear cache success.Press enter key to quit.")
