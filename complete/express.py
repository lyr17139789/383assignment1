import os
# read the csv file exp file:csv_example new csv file:csv_examples
import csv
import random,string
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = "158120.Moodle@gmail.com"
password = "moodle123"

os.system("sudo pip3 install pandas")
print("panas install finished")

import pandas as pd
import pymysql


with open('StudentData.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)
n=10000
m=1000000
num=len(list_of_students)
s = string.ascii_lowercase
adr=[]
pas=[]
pasftp=[]
for i in range(100000,999999):
    pasftp.append(i)
pasftp=random.sample(pasftp,len(list_of_students))
for i in random.sample(range(1,n),n-1):
    if len(str(i))>=4 and len(adr)<num:
        adr.append(str(i)+random.choice(s))
for i in random.sample(range(1,m),m-1):
    if len(str(i))>=6 and len(pas)<num:
        pas.append(str(i))
data = pd.read_csv(r'StudentData.csv')
data1 = adr
data2 = pas
data3 = pasftp
data['moodle_name'] = data1
data['password'] = data2
data['ftppassword'] = data3
data.to_csv(r"StudentDatas.csv",mode = 'a',index =False)
with open('StudentDatas.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        # create empty list
        list_of_students = []
        # for each student, append as list to list (list of lists)
        for row in reader:
                list_of_students.append(row)
                # Remove metadata from top row
        list_of_students.pop(0)

os.system("sudo cp -R /var/383assignment1/complete/StudentDatas.csv /var/www/html/cgi-bin")


print("new csv file finish")



# find external ip
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()


sqlip = open('ip.txt',"r")
a = sqlip.read()
sqlip.close()
print(a)

conn = pymysql.connect(host=a,port=3306, user='root',passwd='Moodle123moodle')
cursor=conn.cursor()



print(list_of_students)
os.chdir("/var")
for i in list_of_students:
        if os.path.exists("/mnt/moodledata/data"+str(i[0])) or i[0]=="student id":
            print("exits data%s"%(i[0]))
        else:
                str1="create database student%s default character set utf8 collate utf8_general_ci;"%i[0]
                print(str1)
                SQLcmd1=cursor.execute(str1)
                str2="create user %s@'%%' identified by '%s';"%(i[4],i[5])
                print(str2)
                SQLcmd3=cursor.execute(str2)
                str3="GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON student%s.* TO %s@'%%' IDENTIFIED BY '%s';"%(i[0],i[4],i[5])
                SQLcmd4=cursor.execute(str3)
                SQLcmd6=cursor.execute("flush privileges;")
conn.commit()
cursor.close()
conn.close()
print("create mysql user finished")




count=0
for i in list_of_students:
        os.system("sudo cp -R /opt/moodle /var/www/html/"+str(i[4]))


        os.chdir("/var")
        if os.path.exists("/mnt/moodledata/data"+str(i[0])) or i[0]=="student id":
            print("exits")
        else:

            os.system("mkdir /mnt/moodledata/data"+str(i[0]))

            os.chdir("/var/www/html/")

            os.system("sudo chown -R www-data /var/data"+str(i[0]))
            os.system("sudo chmod -R 777 /var/data"+str(i[0]))
            os.chdir("/var/www/html/")
            os.chmod(str(i[4]),777)
            os.chdir(str(i[4]))
            if os.path.isfile("config.php"):
                    os.system("rm -rf config.php")
            os.system("""sudo /usr/bin/php admin/cli/install.php --wwwroot=http://"""+str(ip)+"/"+str(i[4])+""" --dataroot=/var/data"""+str(i[0])+""" --dbtype=mysqli --dbhost="""+a+""" --dbname=student"""+str(i[0])+""" --dbuser="""+str(i[4])+""" --dbpass="""+str(i[5])+""" --fullname="""+str(i[4])+"""moodle --shortname=120moodle --adminpass="""+str(i[5])+""" --non-interactive --agree-license""")



            os.system("useradd -m %s"%(i[0]))
            os.system("echo %s:%s| chpasswd"%(i[0],str(i[6])))
            os.system("chown -R %s:%s /var/www/html/%s"%(i[0],i[0],i[4]))
            os.system("chmod -R 777 /home/%s"%(i[0]))

            os.system("touch /etc/userconfig/"+i[0])

            user = open("/etc/userconfig/"+i[0], "w")
            user.write("local_root=/var/www/html/"+i[4])

            user.close()
            count=count+1
            os.system("sudo chmod -R 777 /var/www/html")
            print("loop finish for data%s"%(i[0]))

#send an email with user login info
            message = MIMEMultipart("alternative")
            message["Subject"] = "Moodle account information"
            message["From"] = sender_email
            message["To"] = str(i[3])


            text = """
                FTP server login information:
                Username: """ + str(i[0]) + """
                Password: """ + str(i[6]) + """
                phpMyAdmin login information:
                Username: """ + str(i[4]) + """
                Password: """ + str(i[5])+ """
                Access your Moodle site through this URL:"""+ 'http://'+str(ip)+'/'+str(i[4]) + """
                and the admin login information:
                Username: admin
                Password: """ + str(i[5])

            part1 = MIMEText(text, "plain")
            message.attach(part1)
            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                            sender_email, str(i[3]), message.as_string()
            )
