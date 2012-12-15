#!/bin/bash

##
# Simple Script to convert VOB Files to AVI Files using execflow
# This script is configured to be used with dvd::rip
##

execflow -n 19 transcode -H 10 -a 2 -x vob -i $1 -w 4739,50 -b 128,0,2 -s 2.101 --a52_drc_off -f 25.000 -Y 4,8,4,8 -B 27,10,8 -R 2 -y xvid -o $2/out.avi --progress_meter 2 --progress_rate 25
