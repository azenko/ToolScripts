#!/usr/bin/python
import os, time

tmp_dir = "/tmp/"

sql_host = "127.0.0.1"
sql_user = "root"
sql_password = ""

datetime = time.strftime("%d%m%Y_%H%M%S")
passphrase = "<THE_BORGBACKUP_PASSPHRASE>"

os.system("mkdir " + tmp_dir + datetime)
os.system("mysqldump --host=" + sql_host + " --user=" + sql_user + " --password=" + sql_password + " --all-databases > " + tmp_dir + datetime +
"/database.sql")
os.system("mkdir " + tmp_dir + datetime + "/wordpress")
os.system("cp -R /opt/wordpress/* " + tmp_dir + datetime + "/wordpress")
os.system("export BORG_PASSPHRASE="+passphrase)
os.system("borgbackup create /opt/cBackup::mf_"+datetime+"_full " + tmp_dir)
