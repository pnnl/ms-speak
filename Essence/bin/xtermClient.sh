#!/bin/sh
cd PacketGeneration
python TcpClient.py -i 10.0.0.1 -p 5555 -m v3/PP/PingURL.xml
cd ..

