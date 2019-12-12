from subprocess import Popen
import psutil
import os

username = ""
password = ""
address = ""

# changed by setup script
cur_dir = "CWD"

with open(cur_dir + "/config.txt", "r") as config_file:
    for line in config_file:
        line = line.replace("\n","")
        if line[0:7] == "address":
            address = line[8:]
        elif line[0:8] == "username":
            username = line[9:]
        elif line[0:8] == "password":
            password = line[9:]


# run it as a daemon
command = ['python', cur_dir + '/nightminer.py', '-o', address, '-u', username, '-p', password, '-B', '-q']
new_proc = Popen(command)
