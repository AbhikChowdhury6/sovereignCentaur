#!/bin/bash
#t="$(date +"%d-%m-%Y-%H-%M-%S.%N")"
t="$(date +"%s.%N")"
name=/home/pi/$1-$2-$t
echo $name
raspivid -t 0 -n -w 1440 -h 1440 $3 $4 $5 $6 -ih -fl -fps 30 -o $name.h264
