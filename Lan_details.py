import os
from socket import *
import urllib2
print"""

        l           a      n    n 
        l          a  a    n n  n
        l         aaaaaa   n  n n
        l        a      a  n   nn 
        l l l l a        a n    n


        """

ip=gethostbyname(gethostname())
pp=urllib2.urlopen('https://api.ipify.org?format=json').read()
pp=eval(pp).get("ip")

print "\tPrivate IP : %s\n\tPublic IP  : %s\n\tHostname   : %s"%(ip,pp,gethostbyaddr(ip)[0] )

print"\n\tFinding other devices...."

val=ip.split(".")
for i in range(17,256):
    val[3]=str(i)
    x='.'.join(val)
    r=os.system("ping "+x+' -n 1')
    try:
        if not r:
            name=gethostbyaddr(x)[0]
            print "\t ",x,' ',name
    except:
        pass
