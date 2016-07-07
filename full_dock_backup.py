#!/usr/bin/python

from docker import Client
import os
import time

cli = Client(base_url='unix://var/run/docker.sock')

cont_list = cli.containers()

for cont in cont_list:
        id_cont = cont[u'Id'][0:12]
        name_cont = cont[u'Labels']
        name_cont = name_cont[u'com.docker.compose.project'] + "_"+name_cont[u'com.docker.compose.service'] + "_"+name_cont[u'com.docker.compose.container-number']
        print "Now Backuping : " + id_cont + " - " + name_cont
        os.system("docker commit -p " + id_cont + " " + name_cont)
        os.system("docker save -o /opt/fullBackup/" + name_cont + ".tar " + name_cont)
        print name_cont + " as now a Backup /opt/fullBackup/" + name_cont + ".tar"

datenow = time.strftime("%d%m%Y.%H%M%S")

os.system("tar cvaf /opt/fullBackup/fullBackup."+datenow+".tar.xz /opt/fullBackup/*.tar")
os.system("rm /opt/fullBackup/*.tar")
