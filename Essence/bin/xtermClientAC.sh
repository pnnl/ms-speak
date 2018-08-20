#!/bin/sh
cd PacketGeneration
python TcpClient.py -i 10.0.0.3 -p 5555 -m v3/PP/PingURL.xml
python TcpClient.py -i 10.0.0.2 -p 5555 -m v3/PP/PingURL.xml
cd ..

