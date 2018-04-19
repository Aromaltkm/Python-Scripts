from ipaddress import *
import urllib
import requests
import http.server
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    start_ip=IPv4Address(str(input("Starting IPv4 Address :  ")))
    end_ip=IPv4Address(str(input("Ending IPv4 Address :  ")))
    print("\n")
    while (start_ip <= end_ip):
        try:
            status=urllib.request.urlopen('http://'+str(start_ip)).getcode()
            if(status==200):
                print(start_ip,200,sep="\t")
        except urllib.error.HTTPError as e:
            if(e.code!=404):
                print(start_ip,e.code,http.server.BaseHTTPRequestHandler.responses[e.code],sep="\t")
            else:
                pass
        except urllib.error.URLError:
            pass
        start_ip+=1
        
except:
    print("Invalid IP")


#req=urllib.request.Request("http://210.212.227.210",headers={'User-Agent': 'Mozilla/5.0'})
