#!/bin/bash

loggingFileName=$1
ip=$2
name=$3


#start an IMU process
    #if it crashes restart it and echo failed name
    #if it runs for 15 seconds echo the name and running


#ideal dashboard
    #all in order with their status

until python2 $loggingFileName $ip $name; do
    echo "$name failed, restarting......"
    sleep 1
done