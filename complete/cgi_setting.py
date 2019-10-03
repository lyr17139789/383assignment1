import os

cgi_conf = open('/var/383assignment1/complete/cgi_conf.txt',"r")
new_content = cgi_conf.read()
cgi_conf.close()
os.system("sudo chmod a+w /etc/apache2/sites-enabled/000-default.conf")
modified = open('/etc/apache2/sites-enabled/000-default.conf',"w")
modified.write(new_content)
modified.close()
os.system("sudo chmod a-w /etc/apache2/sites-enabled/000-default.conf")
os.system("sudo ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/")
os.system("sudo ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/")
os.system("service apache2 restart")
os.system("sudo apt install dos2unix")