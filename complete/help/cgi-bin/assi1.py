#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import pymysql
import os
# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import string

import pandas as pd
import pymysql

r = os.popen("curl ifconfig.me")
exip = r.read()
r.close()
f = open("../../ip.txt","r")
ip = f.read()
f.close() 

with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)	
print("Content-type: text/html\n")
print("<title>Assignment1 progress<</title>")
print("<head>")
print("<style type='text/css'>")
print("th,td{border:2px solid black;}")
print("table{padding: 60px 50px;}")
print("input:hover { background-color:green; /* Green */    color: white;border-radius: 50%;}")
print("input {color: green; text-align: left; text-decoration: none; display: inline-block; font-size: 1
6px;border: 2px solid #4CAF50;border-radius: 50%;}")
print("body {background:url('http://blog.hostbaby.com/wp-content/uploads/2014/03/PaintSquares_1400x900-1
024x658.jpg');background-size:98% 100%;background-repeat:no-repeat; }")
print("h1{text-shadow: 5px 5px 5px #95CACA;text-align:center;text-decoration:overline;letter-spacing:2px
;")
print("</style>")
print("</head>")
print("<body><center>")
print("<table>")
print("<tr><th>ID/task</th><th>first</th><th>second</th><th>third</th><th>forth</th><th>fifth</th><th>sixth</th><th>seventh</th></tr>")
for i in list_of_students:
	print("<script type='text/javascript'>")
    print("var btn = document.getElementById('btn')")
    print("btn.onclick=function(){window.location.href='http://'+str(exip)+'/'+str(i[4])+''}")
	print("<tr>")
	print("<td><button id='btn'>student'+str(i[0])+'</button></td>")
	# get post data
	form = cgi.FieldStorage()
	# query to check password and get permissions
	sql = 'select count(*) from mdl_course'
	sq1= 'select count(*) from mdl_user'
	sq2= 'SELECT 1 FROM mdl_user WHERE password="123" and username="Betty Birch" and idnumber="bbirch" and email="bettybirch120@gmail.com"'
	sq3='SELECT 1 FROM `mdl_user` WHERE picture!=0'
	sq5="SELECT 1 FROM `mdl_assign_submission` WHERE status='submitted'"
	sq6="SELECT DISTINCT(userid) FROM mdl_forum_discussions"
	sq7="SELECT 1 FROM mdl_url"
	sq8="SELECT 1 FROM `mdl_files` WHERE component='mod_resource'"
	# connect to database
	conn = pymysql.connect(host=ip,user="root",password="Moodle123moodle",db =""+str(i[4])+"",chars
	et ="utf8")
	#1
	cursor = conn.cursor()
	cursor.execute(sql)
	courses = cursor.fetchall()
	for num in courses:
		if num >= 2:
		   print("<th>ok</th>")
		else:
		   print("<th>no</th>")
	#2
	cursor1 = conn.cursor()
	cursor1.execute(sq1)
	user=cursor1.fetchall()
	cursor2 = conn.cursor()
	cursor2.execute(sq2)
	spe=cursor2.fetchall()
	for num1 in user:
		  if num1 >= 4 and len(spe)!=0 :
			   print("<th>ok</th>")
		  else:
			   print("<th>no</th>")
	#3
	cursor3 = conn.cursor()
	cursor3.execute(sq3)
	pic=cursor3.fetchall()
	if len(pic)!=0:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
	#5
	cursor5 = conn.cursor()
	cursor5.execute(sq5)
	sub=cursor5.fetchall()
	if len(sub)>=2:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
	#6
	cursor6 = conn.cursor()
	cursor6.execute(sq6)
	forum=cursor6.fetchall()
	if len(forum)>=2:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
	#7
	cursor8 = conn.cursor()
	cursor8.execute(sq7)
	files=cursor8.fetchall()
	if len(files)>= 1:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
	#8
	cursor7 = conn.cursor()
	cursor7.execute(sq7)
	url=cursor7.fetchall()
	if len(url)>= 1:
		print("<th>ok</th>")
	else:
		print("<th>no</th>")
	print("</tr>")
print("</table>")
print("""
<form action="../login.html" method="GET">
    <input type="submit" value="Back to progress">
</form>
""")
print('</center></body>')