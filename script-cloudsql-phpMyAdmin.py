import os
os.system("wget https://files.phpmyadmin.net/phpMyAdmin/4.6.3/phpMyAdmin-4.6.3-all-languages.tar.bz2 ")
os.system("mkdir phpMyAdmin")
os.system("tar -xvf phpMyAdmin-4.6.3-all-languages.tar.bz2 -C phpMyAdmin --strip-components=1")

os.chdir("/home/liyueran_spark/phpMyAdmin")
os.system("sudo touch app.yaml")
os.system("sudo chmod o+r /home/liyueran_spark/phpMyAdmin/app.yaml")
os.system("sudo chmod o+w /home/liyueran_spark/phpMyAdmin/app.yaml")
yaml="service: default\nruntime: php55\napi_version: 1\n\nhandlers:\n\n- url: /(.+\.(ico|jpg|png|gif))$\n  static_files: \\1\n  upload: (.+\.(ico|jpg|png|gif))$\n  application_readable: true\n\n- url: /(.+\.(htm|html|css|js))$\n  static_files: \\1\n  upload: (.+\.(htm|html|css|js))$\n  application_readable: true\n\n- url: /(.+\.php)$\n  script: \\1\n  login: admin\n\n- url: /.*\n  script: index.php\n  login: admin"
Modified_file_1 = open('/home/liyueran_spark/phpMyAdmin/app.yaml',"w")
Modified_file_1.write(yaml)
Modified_file_1.close()


os.chdir("/home/liyueran_spark/phpMyAdmin")
os.system("touch config.inc.php")
os.system("sudo chmod o+r /home/liyueran_spark/phpMyAdmin/config.inc.php")
os.system("sudo chmod o+w /home/liyueran_spark/phpMyAdmin/config.inc.php")
config="<?php\n$cfg[\'blowfish_secret\'] = 'phpMyAdmin';\n\n$i = 0;\n\n// Change this to use the project and instance that you've created.\n$host = '/cloudsql/even-ally-254102:us-central1:moodle-db';\n$type = 'socket';\n\n$i++;\n\n$cfg['Servers'][$i]['auth_type'] = 'cookie';\n\n$cfg['Servers'][$i]['socket'] = $host;\n$cfg['Servers'][$i]['connect_type'] = $type;\n$cfg['Servers'][$i]['compress'] = false;\n\n$cfg['Servers'][$i]['extension'] = 'mysqli';\n$cfg['Servers'][$i]['AllowNoPassword'] = true;\n\n$cfg['UploadDir'] = '';\n$cfg['SaveDir'] = '';\n\n$cfg['PmaNoRelation_DisableWarning'] = true;\n$cfg['ExecTimeLimit'] = 60;\n$cfg['CheckConfigurationPermissions'] = false;"
Modified_file_2 = open('/home/liyueran_spark/phpMyAdmin/config.inc.php',"w")
Modified_file_2.write(config)
Modified_file_2.close()


os.chdir("/home/liyueran_spark/phpMyAdmin")
os.system("touch php.ini")
os.system("sudo chmod o+r /home/liyueran_spark/phpMyAdmin/php.ini")
os.system("sudo chmod o+w /home/liyueran_spark/phpMyAdmin/php.ini")
php="google_app_engine.enable_functions = \"php_uname, getmypid\""
Modified_file_3 = open('/home/liyueran_spark/phpMyAdmin/php.ini',"w")
Modified_file_3.write(php)
Modified_file_3.close()


os.system("sudo /google/google-cloud-sdk/bin/gcloud components update")
os.system("sudo /google/google-cloud-sdk/bin/gcloud app deploy")


