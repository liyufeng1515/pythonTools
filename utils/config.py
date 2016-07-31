#encoding=utf-8
import sys

username = 
password = 
olapIP80 = 
olapIP90 = 
megatronIP80 = 
erpIP80 = 
webIP90 = 

def requiredParameter(param):
	if None==param:
		raw_input("\nRequired parameter is missing. Press enter key to quit.")
		sys.exit(0)

def loginUrl(ip):
        requiredParameter(ip)
	return ""


def loginHttpsUrl(ip):
        requiredParameter(ip)
	return ""

def clearCacheUrl(ip):
	requiredParameter(ip)
	return ""

def clearCacheHttpsUrl(ip):
        requiredParameter(ip)
	return ""	

def entityUrl(ip):
        requiredParameter(ip)
        return ""

def serviceUrl(ip):
        requiredParameter(ip)
        return ""	
