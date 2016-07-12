#!/usr/bin/python
import os, time

tmp_dir = "/tmp/"

sql_host = "127.0.0.1"
sql_user = "root"
sql_password = ""

datetime = time.strftime("%d%m%Y_%H%M%S")

os.system("mkdir " + tmp_dir + datetime)
os.system("mysqldump --host="+sql_host+" --user="+sql_user+" --password="+sql_password+" --all-databases > " + tmp_dir + datetime +
"/database.sql")
os.system("mkdir " + tmp_dir + datetime + "/wordpress")
os.system("cp -R /opt/mf-wordpress/* " + tmp_dir + datetime + "/wordpress")
os.system("tar czf /opt/fBackup/backup." + datetime + ".tar.gz " + tmp_dir + datetime + "/")
os.system("rm " + tmp_dir + datetime + "/ -r")
