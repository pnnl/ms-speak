#!/bin/sh
cd PacketGeneration
python SockServer.py -i 10.0.0.1 -p 5555 -d v3
cd ..

