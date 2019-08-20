import os
os.system("sudo apt-get install vim")
os.system("sudo apt install apache2 mysql-client mysql-server php libapache2-mod-php")

os.system("sudo apt install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
print("Install Additional Software finished")

os.system("sudo service apache2 restart")

os.system("sudo apt install git")
print("git download finished")

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


import random


os.system("sudo -s")
os.system("apt-get install vsftpd")
r = os.popen("curl ifconfig.me")
ip = r.read()
r.close()

os.chdir("/var/383assignment1/complete/")
ftp_conf = open('ftp_conf.txt',"r")
new_content = ftp_conf.read()
ftp_conf.close()
position=new_content.find("/etc/pam.d/vsftpd")
modified= open('/etc/vsftpd.conf',"w")
modified.write(new_content[0:position]+"\n"+"pasv_address="+ip)
modified.close()
os.system("chmod a-w /var/www/html")

pam = open('/etc/pam.d/vsftpd',"w")
pam.write(new_content[position+18:len(new_content)])
pam.close()

os.mkdir("/etc/userconfig")

os.system("useradd -m teacher")
os.system("echo teacher:teacher| chpasswd")
os.system("chown -R teacher /var/www/html")
os.system("chmod -R 777 /home/teacher")
os.system("touch /etc/userconfig/teacher")
user = open("/etc/userconfig/teacher", "w")
user.write("local_root=/var/www/html/")
user.close()

os.system("sudo service vsftpd restart")

os.chdir("/var/www/html")
os.system("sudo wget https://files.phpmyadmin.net/phpMyAdmin/4.7.0/phpMyAdmin-4.7.0-all-languages.zip")
os.system("sudo unzip phpMyAdmin-4.7.0-all-languages.zip")
os.system("sudo mv phpMyAdmin-4.7.0-all-languages phpMyAdmin")
os.chdir("/var/www/html/phpMyAdmin")
os.system("sudo mv config.sample.inc.php  config.inc.php")

os.system("sudo chmod o+w config.inc.php")


phpfile = open('/var/www/html/phpMyAdmin/config.inc.php',"r")
content = phpfile.read()
phpfile.close()

position=content.find("blowfish_secret")
length = len("blowfish_secret")
position=position+length

pwd='itcapstone'

if position != -1:
	content = content[:position+4] + "\'" + pwd +"\'" + content[position+8:]
	Modified_file = open('/phpMyAdmin/phpMyAdmin-4.7.0-all-languages/config.inc.php',"w")
	Modified_file.write(content)
	Modified_file.close()
	print("the file has been modified")
os.system("sudo chmod o-w config.inc.php")

os.chdir("/etc/apache2/conf-available")
os.system("sudo touch phpMyAdmin.conf")
os.system("sudo chmod o+w phpMyAdmin.conf")

configuration="Alias /phpMyAdmin \"/var/www/html/phpMyAdmin/\" \n<Directory \"/var/www/html/phpMyAdmin/\"> \nOptions Indexes FollowSymLinks MultiViews \nAllowOverride all \nRequire all granted \nphp_admin_value upload_max_filesize 128M \nphp_admin_value post_max_size 128M \nphp_admin_value max_execution_time 360 \nphp_admin_value max_input_time 360 \n</Directory>"


conf_file = open('/etc/apache2/conf-available/phpMyAdmin.php',"w")
conf_file.write(configuration)
conf_file.close()


os.system("sudo chmod o-w phpMyAdmin.php")
os.system("sudo /etc/init.d/apache2 restart")

os.chdir("/var/383assignment1/complete/")
os.system("python3 for_loop.py")
print("for_loop finished")
