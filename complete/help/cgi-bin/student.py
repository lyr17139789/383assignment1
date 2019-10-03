#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi


list=[["try.html",0,9]]
def match_site(name):
    for i in list:
        if i[0] ==name:
            print('<script type="text/javascript"> ')
            print("location.href ='http://' + window.location.href.split('/')[2]+'/'+'%s';"%name)
            print('</script>')

        else:
            print("Your site name is wrong ,please check it")
            print("""
            <form action="../student.html" method="GET">
                <input type="submit" value="Back to Home page">
            </form>
            """)




print("Content-type: text/html\n")
print("<title>Result</title>")
print("<body><center>")

form = cgi.FieldStorage()
name = form['id'].value if 'id' in form else ''
match_site(name)

print('</center></body>')