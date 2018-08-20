#!/bin/bash
i="0"
while [ $i -lt 1000 ]
do
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
i=$[$i+1]
sleep 0.1s
done

sleep 300s

j="0"
while [ $j -lt 1000 ]
do
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
./xtermClient.sh
j=$[$j+1]
sleep 0.1s
done

