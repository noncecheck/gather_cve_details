#AUTHOR : ARUN MOOTHEDATH
#EMAIL : curtissoflow@gmail.com
#Date: 6/15/2022

import json
import re
#import attackerkb_api - Install - pip3 install attackerkb_api
from attackerkb_api import AttackerKB
#INSERT YOUR KEY HERE
API_KEY = "MWQ3YjZhNDktZjRlZi00YTA3LWFjMDMtYzY2YTdjYmNmNTMxOnRmYjBZdGMtZGNUMHM3b2JDWjVqXzVjVTRjUlF4djE1YmhvUHpTM3FvZTg9"
api = AttackerKB(API_KEY)

#Get CVE Details
def getCVEDetails(cve):
	result = api.get_topics(name=cve)
	return result

#Get CVE Input
while True:
	cvename = input("Please enter a CVE: ")
	cve_pattern = 'CVE-\d{4}-\d{4,7}'
	cves = re.findall(cve_pattern, cvename)
	if len(cves) <1:
		print("Please enter a valid CVE!")
		continue
	else:
		cvedetails = getCVEDetails(cvename)
		trimmedcve = cvedetails[0]
		dumpcve = json.dumps(trimmedcve, indent=4, sort_keys=True)
		print(dumpcve)
		#Cleanup unicode strings 'u'
		final_dictionary = json.loads(dumpcve.encode("ascii"))
		#Extract required fields
		date_created = final_dictionary["created"]
		v_title = final_dictionary["name"]
		document = final_dictionary["document"]
		metadata = final_dictionary["metadata"]
		product_names = metadata['vendor']['productNames'][0]
		vendor_names = metadata['vendor']['vendorNames'][0]
		score = final_dictionary["score"]
		attackerValue = score['attackerValue']
		exploit = score['exploitability']
		finalout = "Title :"+ v_title + "\nDocument: " + document + "\nProduct Name : "+ product_names + "\nVendor Names : "+ vendor_names+"\nAttacker Value : "+ str(attackerValue)+"\nExploitability : "+str(exploit)
		#print(finalout)
		break



