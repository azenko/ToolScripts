#!/usr/bin/python
import os, time

tmp_dir = "/tmp/bck/"

datetime = time.strftime("%d%m%Y_%H%M%S")
passphrase = "<THE_BORGBACK_PASSPHRASE>"

os.system("mkdir " + tmp_dir + datetime)
os.system("mysqldump --host=127.0.0.1 --user=root --password=<THE_PASSWORD> --all-databases > " + tmp_dir + datetime +
"/database.sql")
os.system("mkdir " + tmp_dir + datetime + "/wordpress")
os.system("cp -R /opt/wordpress/* " + tmp_dir + datetime + "/wordpress")
os.system("export BORG_PASSPHRASE="+passphrase)
os.system("borgbackup create /opt/cBackup::mf_"+datetime+"_full /tmp/bck/")
