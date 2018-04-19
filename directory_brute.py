import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print """


            DIRECTORY FINDER


            """

f=open("file1.wordlist")
words=f.read()
words=words.split('\n')
url=raw_input("Enter the website eg :  https://example.com\n\n\t\t.....=> ")
print "\nURLS are :",
working=[]
for i in words:
    url1=url+'/'+i
    print '\n\t'+'. '+url1,
    try:
        x=requests.get(url,verify=False).status_code
        print "************200",
    except:
        print "************404",
print '\n\n WORKING URLS : '
for i in working:
    print '\t'+i
v=raw_input("\nPress Enter to exit.......")
    
