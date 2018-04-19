import mechanize, itertools,urllib2

from bs4 import BeautifulSoup
combos =["abc","jkhgkgk","MIBLI"]
br=mechanize.Browser()
url="http://210.212.227.210/tkmce/"
br.open(url)


"""form=br.forms()
or f in form:
    print f"""

br.select_form(nr=0)
br.form['txtUserName']='151000'
br.form['txtPassword']='MIBLI'
br.method='POST'
br.submit()

for link in br.links():
    if link.text=="Student- Subject / datewise Attendance View":
        request=br.click_link(link)
        response=br.follow_link(link)
        break

#form=br.forms()
#for f in form:
#    print f,'\n\n'

br.select_form(nr=0)
br.form['ctl00$ContentPlaceHolder1$txtFromdate']='10/05/2017'
br.form['ctl00$ContentPlaceHolder1$txtToDate']='17/05/2017'
br.method='POST'
r=br.submit('ctl00$ContentPlaceHolder1$btnSearch')

soup=BeautifulSoup(r,'html.parser')
table=soup.find("td",colspan="6")
#print(table)
rows=table.find_all('tr')
data=[]
for i in rows[3:10]:
    val=[]
    for col in i.find_all('td'):
        col=str(col)
        val.append(col[4:len(col)-5])
         
    data.append(val)

print data
#f=0

"""for i in combos:
    print(i)
    br.select_form(nr=0)
    x=''.join(i)
    br.form['txtUserName']='151000'
    br.form['txtPassword']=x
    br.method="POST"
    print(x)
    response=br.submit()
    
    if response.geturl()!=url:
        f=1
        print"FOUND    "+x
        break
if f==0:
    print "NOT FOUND"""







#combos = itertools.permutations("i3^4hUP-",8)
