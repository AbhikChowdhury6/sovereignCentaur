#!/bin/bash

loggingFileName="/home/chowder/Documents/universalos/IMUlog.py"


trap 'kill %1; kill %2; kill %3; kill %4; kill %5; kill %6; kill %7; kill %8; kill %9; kill %10' SIGINT
bash IMURun.sh $loggingFileName 192.168.0.249 leftAnkle &
bash IMURun.sh $loggingFileName 192.168.0.100 rightAnkle &
bash IMURun.sh $loggingFileName 192.168.0.104 leftThigh &
bash IMURun.sh $loggingFileName 192.168.0.220 rightThigh &
bash IMURun.sh $loggingFileName 192.168.0.236 leftForearm &
bash IMURun.sh $loggingFileName 192.168.0.106 rightForearm &
bash IMURun.sh $loggingFileName 192.168.0.248 leftBicep &
bash IMURun.sh $loggingFileName 192.168.0.244 rightBicep &
bash IMURun.sh $loggingFileName 192.168.0.155 upperBack &
bash IMURun.sh $loggingFileName 192.168.0.136 middleChest &
bash IMURun.sh $loggingFileName 192.168.0.211 backHip