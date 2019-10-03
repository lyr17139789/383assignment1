#!/usr/bin/python3
print("Content-type:text/html\n\n")
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-packages")
import cgi
import os
import csv
import pymysql

sqlip = open('../../ip.txt',"r")
a = sqlip.read()
sqlip.close()
print(a)


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

def modify_csv(num,id,password):
    students = Student_list("StudentDatas.csv")
    if num=="ftp":
        students[id-1][6]=password
    elif  num=="phpmyadmin":
        students[id - 1][5]=password
    else:
        return
    os.system("sudo rm -rf StudentDatas.csv")
    with open('StudentDatas.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for row in students:
            writer.writerow(row)

def confirm_permission(student_list,teacher, app, username, pwd):
    count=0
    for student in student_list:
        if teacher == student[3]:
            if app == "ftp":
                if username==student[0]:
                    ftp_change(username, pwd)
                    print("Modify successfully!  (*^▽^*)")

                else:
                    print("Please check your account!")

            elif app == "phpmyadmin":
                if username == student[4]:
                    phpma_change(username, pwd)
                    print("Modify successfully!  (*^▽^*)")
                else:
                    print("Please check your account!")

            elif app == "moodle":
                if username == student[4]:
                    moodle_change(username, pwd)
                    print("Modify successfully!  (*^▽^*)")
                else:
                    print("Please check your account!")
        else:
            count=count+1

        if count==len(student_list):
            print("Your email does not exist,please check it!")
    print("""
            <form action="../student.html" method="GET">
                            <input type="submit" value="Back to home page">
                        </form>
                        """)


def ftp_change(username, pwd):
    os.system("sudo echo s1:1234| chpasswd")


def phpma_change(username, pwd):

    conn = pymysql.connect(host=a,port=3306, user='root',passwd='Moodle123moodle')
    cursor=conn.cursor()

    str1 = "alter user %s@'%%' identified by '%s';" % (username, str(pwd))
    print(str1)
    SQLcmd1 = cursor.execute(str1)
    SQLcmd6 = cursor.execute("flush privileges;")
    conn.commit()
    cursor.close()
    conn.close()
    print("!!!!!!!!!!!!!!!!!!!!!!")


def moodle_change(username,pwd):

    conn = pymysql.connect(host=a,port=3306, user='root',passwd='Moodle123moodle')
    cursor=conn.cursor()

    sql2="use %s "%username
    a= cursor.execute(sql2)
    print(sql2)
    sql = "UPDATE mdl_user SET `password` =MD5(%s) WHERE `username` = 'admin';"%pwd
    b=cursor.execute(sql)
    c=cursor.execute("flush privileges;")
    conn.commit()
    cursor.close()
    conn.close()
    print(cursor.rowcount, "record(s) affected")


print("<title>Result</title>")
print("<body><center>")

form = cgi.FieldStorage()
sid = form['sid'].value if 'sid' in form else ''
teacher = form['teacher'].value if 'teacher' in form else ''
app = form['app'].value if 'app' in form else ''
username = form['account'].value if 'account' in form else ''
pwd = form['pwd'].value if 'pwd' in form else ''
students=Student_list("StudentDatas.csv")
confirm_permission(students,teacher, app, username, pwd)
modify_csv(app,sid,pwd)
print(app)
print('</center></body>')
