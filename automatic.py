# we assumpt that users alredy download python3-pip 
import os


os.chdir("/opt")
os.system("sudo git clone https://github.com/moodle/moodle.git")
os.chdir("/opt/moodle")
os.system("sudo git branch -a")
os.system("sudo git branch -track MOODLE_36_STABLE origin/MOODLE_36_STABLE")
os.system("sudo git checkout MOODLE_36_STABLE ")

print("moodle download finished")

os.system("sudo cp -R /opt/moodle /var/www/html/")
os.system("sudo mkdir /var/moodledata")
os.system("sudo chown -R www-data /var/moodledata")
os.system("sudo chmod -R 777 /var/moodledata")
os.system("chmod -R 0755 /var/www/html/moodle ")

print("copy local repository finished")


#modify mysql configuration file

os.chdir("/etc/mysql/mysql.conf.d/")
#add permission write to the file
os.system("sudo chmod o+w mysqld.cnf ")


data="\ndefault_storage_engine = innodb\ninnodb_file_per_table = 1\ninnodb_file_format = Barracuda"

Sqlfile = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"r")
content = Sqlfile.read()
Sqlfile.close()

position=content.find("skip-external-locking")
length = len("skip-external-locking")
if position != -1:
	content = content[:position+length] + data + content[position+length:]
	Modified_file = open('/etc/mysql/mysql.conf.d/mysqld.cnf',"w")
	Modified_file.write(content)
	Modified_file.close()
	print("the file has been modified")

#change the permission back
os.system("sudo chmod o-w mysqld.cnf ")

os.system("sudo service mysql restart")
os.system("sudo mysql -u root -p")

#moodle mysql
os.system("sudo pip3 install pymysql")

import pymysql

os.chdir("/etc/mysql/mysql.conf.d/")

#find the top level passwd

os.chdir('/etc/mysql/')
os.system("sudo chmod o+w debian.cnf")
os.system("sudo chmod o+r debian.cnf")

data=""
pwdfile = open('/etc/mysql/debian.cnf',"r")
pwdcontent = pwdfile.read()

pos = pwdcontent.find("[mysql_upgrade]\nhost     = localhost")
lenth=len('[mysql_upgrade]\nhost     = localhost')
UAP=(pwdcontent[pos+lenth:])

pos_user=UAP.find('user     = ')
pos_pwd=UAP.find('password = ')
pos_socket=UAP.find('socket')

TopUser=UAP[pos_user+len('user     = '):pos_pwd]
TopPwd=UAP[pos_pwd+len('password = '):pos_socket]


os.system("sudo chmod o-w debian.cnf")
os.system("sudo chmod o-r debian.cnf")

#god passwd(top level) for this computer
#user     = debian-sys-maint
#password = 0A7XW7QUpbRYhllT


conn = pymysql.connect(host='127.0.0.1',port=3306, user=TopUser,passwd=TopPwd)
cursor=conn.cursor()


SQLcmd1=cursor.execute("use moodle;")

SQLcmd2=cursor.execute("flush PRIVILEGES;")

SQLcmd3=cursor.execute(" grant all privileges on *.* to 'abcde'@'%' identified by 'Lyr14@Wyc1129';")

SQLcmd4=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON moodle.* TO abcde@localhost IDENTIFIED BY 'Lyr14@Wyc1129';")

conn.commit()
cursor.close()
conn.close


os.system("sudo chmod -R 777 /var/www/html/moodle")
os.system("sudo chmod -R 0755 /var/www/html/moodle")




