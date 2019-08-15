import os
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
