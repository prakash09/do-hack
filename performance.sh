'''#!/bin/bash

CPU=$(grep -c "^processor" /proc/cpuinfo)
LOAD_1=$(cat /proc/loadavg | awk '{print $1}')
LOAD_AVERAGE_1=$(($(echo ${LOAD_1} | awk '{print 100 * $1}') / ${CPU}))
echo $LOAD_AVERAGE_1'''