
import os
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
