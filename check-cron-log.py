#!/usr/bin/env python

from getpass import getuser
from re import split

loglines = []
user = getuser()

f = open("/var/log/cron", 'r')
line = f.readline()
while len(line) != 0:
	if user in line:
		loglines.append(line)
	line = f.readline()


command = split(line, "CMD", 2)
command = command[1]

date_sp = split(line, "localhost", 2)
pid = date_sp[0]
date = date_sp[1]
del date_sp
