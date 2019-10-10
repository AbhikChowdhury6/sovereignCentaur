#!/bin/bash
baseDirectory=$1


# bash /home/chowder/Documents/sovereignCentaur/proprioceptive/proprioseptive.sh /home/chowder/Documents/

runFileName="$baseDirectory/sovereignCentaur/proprioceptive/IMURun.sh"
loggingFileName="$baseDirectory/sovereignCentaur/proprioceptive/IMUlog.py"


trap 'kill %1; kill %2; kill %3; kill %4; kill %5; kill %6; kill %7; kill %8; kill %9; kill %10' SIGINT
bash $runFileName $loggingFileName 192.168.8.136 leftAnkle & #A5 B8
bash $runFileName $loggingFileName 192.168.8.182 rightAnkle & #A8 80
bash $runFileName $loggingFileName 192.168.8.150 leftThigh & #AC C8
bash $runFileName $loggingFileName 192.168.8.236 rightThigh & #56 94
bash $runFileName $loggingFileName 192.168.8.203 leftForearm & #FE F0
bash $runFileName $loggingFileName 192.168.8.215 rightForearm & #DF 78
bash $runFileName $loggingFileName 192.168.8.132 leftBicep & #A3 80
bash $runFileName $loggingFileName 192.168.8.172 rightBicep & #B2 E4
bash $runFileName $loggingFileName 192.168.8.214 upperBack & #AE 10
bash $runFileName $loggingFileName 192.168.8.243 middleChest & #C6 41
bash $runFileName $loggingFileName 192.168.8.138 midBelly #D0 DD
