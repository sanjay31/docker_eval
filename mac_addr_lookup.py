#! python

import urllib.request as urlRq
import json
import sys
import logging
import argparse


logging.basicConfig(level=logging.INFO)



if __name__ == '__main__':
    try:  
        parser = argparse.ArgumentParser(description='MAC Address Look up')

        parser.add_argument('--ApiKey', help='API Key', required=True)
        parser.add_argument('--MacAddress', help='MAC Address', required=True)

        args = parser.parse_args()


        url = 'https://api.macaddress.io/v1?output=json&'


        url = url + 'apiKey=' + args.ApiKey + '&search=' + args.MacAddress 

        #logging.info(url)

        content = json.load(urlRq.urlopen(url))
        companyName = content['vendorDetails']['companyName']

        #print (content)
        print ('Company Name: ' + companyName)

    except Exception as ex:
        print(ex)


