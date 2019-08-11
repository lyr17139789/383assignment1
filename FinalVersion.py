import os
os.system("sudo apt-get install vim")
os.system("sudo apt install apache2 mysql-client mysql-server php libapache2-mod-php")

os.system("sudo apt install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
print("Install Additional Software finished")

os.system("sudo service apache2 restart")

os.system("sudo apt install git")
print("git down;oad finished")

os.system("sudo apt-get install python3-pip")
os.system("sudo pip3 install --upgrade pip")
os.system("sudo pip3 install pymysql")
import pymysql
#import csv
# read the csv file


#start
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

TopUser=UAP[pos_user+len('user     = '):pos_pwd].strip()
TopPwd=UAP[pos_pwd+len('password = '):pos_socket].strip()

os.system("sudo chmod o-w debian.cnf")
os.system("sudo chmod o-r debian.cnf")
print("top pwd find finish",TopUser,TopPwd)

# find external ip
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()

conn = pymysql.connect(host='127.0.0.1',port=3306, user='debian-sys-maint',passwd="lO5k3KdhTU0LoEey")
cursor=conn.cursor()

list_of_students = [[1,'q','a','23'],[2,'w','e','321'],[3,'ttt','hhh','456']]


for i in list_of_students:
        SQLcmd1=cursor.execute("create database student%s default character set utf8 collate utf8_general_ci;",i[0])
        SQLcmd3=cursor.execute(" create user student%s@'%%' identified by %s;",(i[0],i[3]))
        SQLcmd4=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON student%s.* TO student%s@'%%' IDENTIFIED BY %s;",(i[0],i[0],i[3]))
        SQLcmd6=cursor.execute("flush privileges;")
conn.commit()
cursor.close()
conn.close()

for i in list_of_students:
        os.system("sudo cp -R /opt/moodle /var/www/html/"+str(i[0]))
        os.chdir("/var/www/html/")
        os.chmod(str(i[0]),777)
        os.chdir(str(i[0]))
        if os.path.isfile("config.php"):
                os.system("rm -rf config.php")

        os.system("touch config.php ")
        data="<?php  // Moodle configuration file\n" \
                "unset($CFG);\n" \
                "global $CFG;\n" \
                "$CFG = new stdClass();\n" \
                "$CFG->dbtype    = 'mysqli';\n" \
                "$CFG->dblibrary = 'native';\n" \
                "$CFG->dbhost    = 'localhost';\n" \
                "$CFG->dbname    = 'student"+str(i[0])+"';\n" \
                "$CFG->dbuser    = 'student"+str(i[0])+"';\n" \
                "$CFG->dbpass    = '"+str(i[3])+"';\n" \
                "$CFG->prefix    = 'mdl_';\n" \
                "$CFG->dboptions = array (\n" \
                "  'dbpersist' => 0,\n" \
                "  'dbport' => '',\n" \
                "  'dbsocket' => '',\n" \
                "  'dbcollation' => 'utf8mb4_unicode_ci',\n" \
                ");\n" \
                "$CFG->wwwroot   = 'http://"+str(ip)+"/"+str(i[0])+"';\n" \
				"$CFG->dataroot  = '/var/moodledata';\n" \
				"$CFG->admin     = 'admin';\n" \
				"$CFG->directorypermissions = 0777;\n" \
				"require_once(__DIR__ . '/lib/setup.php');\n"
        content = data
        file = open('config.php', "w")
        file.write(content)
        file.close()
