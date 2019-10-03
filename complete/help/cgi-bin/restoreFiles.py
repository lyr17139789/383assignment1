#!/usr/bin/python3
print("Content-type:text/html\n\n")
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import os
import csv
import pymysql


# Import modules for CGI handling





def Student_list(file_name):
    with open(file_name, 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
            list_of_students.append(row)
            # Remove metadata from top row
        list_of_students.pop(0)
    return list_of_students

def confirm(students,app,username,password):
    count=0
    for i in students:
        if app=="file":
            if username==i[0]:
                if password==i[6]:
                    filerestore(i[4])
                else:
                    print("Please check your password")
            else:
                count=count+1
        if app=="mysql":
            if username==i[4]:
                if password==i[5]:
                    sqlrestore("student"+i[0],username,password)
                else:
                    print("Please check your password")
            else:
                count=count+1
        if app=="site":
            if username==i[0]:
                if password==i[6]:
                    siterestore("data"+i[0])
                else:
                    print("Please check your password")
            else:
                count=count+1

    if count==len(students):
        print("Please check your username")
    print("""
            <form action="../student.html" method="GET">
                    <input type="submit" value="Back to Login">
                </form>
                """)




def filerestore(filename):
    # Copy the code directory back to its original location
    os.system("sudo cp -rp /mnt/backup/msbu/%s /var/www/html/%s"%(filename,filename))
    print("Restore sucessfully!!!")

def siterestore(file):
    os.system("sudo cp -rp /mnt/backup/mdbu/%s /mnt/moodledata/%s"%(file,file))
    print("Restore sucessfully!!!")

def sqlrestore(database,username,password):
    ip = open('../../ip.txt', "r")
    a = ip.read()
    ip.close()
    conn = pymysql.connect(host=a, port=3306, user="root", passwd="Moodle123moodle")
    cursor = conn.cursor()
    sql4="DROP DATABASE student%s; "%database
    b = cursor.execute(sql4)
    sql2="create database student%s; "%database
    a= cursor.execute(sql2)
    c=cursor.execute("flush privileges;")
    conn.commit()
    cursor.close()
    conn.close()
    os.system("mysql -h%s -u%s -p%s %s < /mnt/backup/dbbu/%s.sql"%(a,username,password,database,database))
    print("Restore sucessfully!!!")

# def restoreFiles():
#     #Copy moodledata back to its original location
#     os.system("sudo cp -rp ./backup/moodledata/ ./")
#
#     #Copy the code directory back to its original location
#     os.system("sudo cp -rp .backup/moodle ./html/moodle")
#
#     #Login to mysql to restore database
#     os.system("sudo mysql -uroot -pMypassword")
#     os.system("create database moodle")
#     os.system("quit")
#     os.system("mysql -uroot -pMypassword moodle < ./backup/moodle.sql")
#     print("Restoring Files Completed----------------------------------------------")
#
# #If student clicks Restore Button then call backupFiles method
# print("<title>Result</title>")
# print("<body><center>")

form = cgi.FieldStorage()
app = form['app'].value if 'app' in form else ''
username = form['user'].value if 'user' in form else ''
pwd = form['pwd'].value if 'pwd' in form else ''
students=Student_list("StudentDatas.csv")
confirm(students,app,username,password)
