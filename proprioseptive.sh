#!/bin/bash
baseDirectory=$1

runFileName="$baseDirectory/sovereignCentaur/IMURun.sh"
loggingFileName="$baseDirectory/sovereignCentaur/IMUlog.py"


trap 'kill %1; kill %2; kill %3; kill %4; kill %5; kill %6; kill %7; kill %8; kill %9; kill %10' SIGINT
bash $runFileName $loggingFileName 192.168.0.249 leftAnkle &
bash $runFileName $loggingFileName 192.168.0.100 rightAnkle &
bash $runFileName $loggingFileName 192.168.0.104 leftThigh &
bash $runFileName $loggingFileName 192.168.0.220 rightThigh &
bash $runFileName $loggingFileName 192.168.0.236 leftForearm &
bash $runFileName $loggingFileName 192.168.0.106 rightForearm &
bash $runFileName $loggingFileName 192.168.0.248 leftBicep &
bash $runFileName $loggingFileName 192.168.0.244 rightBicep &
bash $runFileName $loggingFileName 192.168.0.155 upperBack &
bash $runFileName $loggingFileName 192.168.0.136 middleChest &
bash $runFileName $loggingFileName 192.168.0.211 backHip
