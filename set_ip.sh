#!/bin/sh
NEW=10.0.0.100
OLD=192.168.1.100

# Set configuration
sed -i "s/$OLD/$NEW/" ./conf/fe.json
sed -i "s/$OLD/$NEW/" ./conf/portal.py
sed -i "s/$OLD/$NEW/" ./conf/alarm.json
