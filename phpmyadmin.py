import os
#os.chdir("/")
#os.system("sudo mkdir phpMyAdmin")


#os.chdir("/phpMyAdmin")

#os.system("sudo wget https://files.phpmyadmin.net/phpMyAdmin/4.7.0/phpMyAdmin-4.7.0-all-languages.zip")
#os.system("sudo unzip phpMyAdmin-4.7.0-all-languages.zip")

#os.chdir("/phpMyAdmin/phpMyAdmin-4.7.0-all-languages")

#os.system("sudo mv config.sample.inc.php  config.inc.php")

#os.system("sudo chmod o+r config.inc.php")
#os.system("sudo chmod o+w config.inc.php")

#phpfile = open('/phpMyAdmin/phpMyAdmin-4.7.0-all-languages/config.inc.php',"r")
#content = phpfile.read()
#phpfile.close()

#position=content.find("blowfish_secret")
#length = len("blowfish_secret")
#position=position+length

#pwd='itcapstone'

#if position != -1:
#	content = content[:position+4] + "\'" + pwd +"\'" + content[position+8:]
#	Modified_file = open('/phpMyAdmin/phpMyAdmin-4.7.0-all-languages/config.inc.php',"w")
#	Modified_file.write(content)
#	Modified_file.close()
#	print("the file has been modified")


#os.system("sudo chmod o-w config.inc.php")

#os.chdir("/etc/apache2/conf-available")
#os.system("sudo touch phpMyAdmin.php")

#os.system("sudo chmod o+r phpMyAdmin.php")
#os.system("sudo chmod o+w phpMyAdmin.php")

#configuration="Alias /phpMyAdmin \"/phpMyAdmin/\" \n<Directory \"/phpMyAdmin/\"> \nOptions Indexes FollowSymLinks MultiViews \nAllowOverride all \nRequire all granted \nphp_admin_value upload_max_filesize 128M \nphp_admin_value post_max_size 128M \nphp_admin_value max_execution_time 360 \nphp_admin_value max_input_time 360 \n</Directory>"


#conf_file = open('/etc/apache2/conf-available/phpMyAdmin.php',"w")
#conf_file.write(configuration)
#conf_file.close()


#os.system("sudo chmod o-w phpMyAdmin.php")

#os.system("sudo /etc/init.d/apache2 restart")

os.chdir("/etc/apache2")
os.system("sudo chmod o+w apache2.conf")
add = '\nInclude conf/phpmyadmin.conf'
addfile = open("/etc/apache2/apache2.conf",'r')
files = addfile.read()
files = files + add
addedfile=open("/etc/apache2/apache2.conf",'w')
addedfile.write(files)
addedfile.close()
os.system("sudo chmod o-w apache2.conf")


