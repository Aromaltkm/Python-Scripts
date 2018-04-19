
import requests

#remove http warning 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("""

            SUB DOMAIN BRUTEFORCER

                                        """)

fname='C:\Python\wordlis.txt'
f=open(fname)
wordlist=f.readlines()
wordlist=[x.rstrip('\n') for x in wordlist]
web=raw_input("Enter your Website eg: https://example.com\n\n\t\t.....=>")
print("\nBruteforcing with sample wordlist.........")
working=[]

k=1
for i in wordlist:
    url=web[:8]+i+'.'+web[8:]
    print k, "out of",len(wordlist), url,   
    try:
            x=requests.get(url,verify=False).status_code
            working.append(url)
            print "............200 OK"
    except:
            print " "
    k+=1

print "\n\n\t*******Bruteforce Results********\n"
j=1
for i in working:
    print '\t'+str(j)+'.'+i
    j+=1
print '\nEnd Of results'


x=raw_input("Press Enter to Exit..........")
