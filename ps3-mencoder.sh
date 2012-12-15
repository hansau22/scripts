#!/bin/bash

##
# Simple Script to convert AVI files to PS3 compatible divx files
##

mencoder -ffourcc DX50 -oac lavc -ovc lavc -ofps 25 -lavcopts vcodec=mpeg4:vbitrate=10000:vhq:keyint=15:acodec=libmp3lame:abitrate=128 -srate 44100 -vf harddup -o $2 $1
