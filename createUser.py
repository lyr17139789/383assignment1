import os
import pymysql

TopUser  = 'debian-sys-maint'
TopPwd = '0A7XW7QUpbRYhllT'

conn = pymysql.connect(host='127.0.0.1',port=3306, user=TopUser,passwd=TopPwd)
cursor=conn.cursor()


for i in range(1,3):
	SQLcmd1=cursor.execute("create database student%s default character set utf8 collate utf8_general_ci;",i)

	SQLcmd2=cursor.execute(" create user teacher%s@'%%' identified by %s;",(i,'Pwd@123456'))

	SQLcmd3=cursor.execute(" create user student%s@'%%' identified by %s;",(i,'Pwd@123456'))

	SQLcmd4=cursor.execute("GRANT SELECT ON student%s.* TO student%s@'%%' IDENTIFIED BY 'Pwd@123456';",(i,i))
	
	SQLcmd5=cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON student%s.* TO teacher%s@'%%' IDENTIFIED BY 'Pwd@123456';",(i,i))

	SQLcmd6=cursor.execute("flush privileges;")

conn.commit()
cursor.close()
conn.close
