from django.shortcuts import render
import subprocess
from api import *
# Create your views here.
def measurePerformance(ip_address):
	bashCommand = "vmstat -s"
	output = subprocess.check_output(['bash','-c', bashCommand])
	x = output.split('\n')
	total_memory = int(x[0].split()[0])
	used_memory = int(x[1].split()[0])
	memory_ratio = used_memory*1.0/total_memory

	bashCommand = '''#!/bin/bash
	CPU=$(grep -c "^processor" /proc/cpuinfo)
	LOAD_1=$(cat /proc/loadavg | awk '{print $1}')
	LOAD_AVERAGE_1=$(($(echo ${LOAD_1} | awk '{print 100 * $1}') / ${CPU}))
	echo $LOAD_AVERAGE_1'''
	output = subprocess.check_output(['bash','-c', bashCommand])
	cpu_usage = int(output.split()[0])

	performance = {
		"memory":memory_ratio,
		"cpu":cpu_usage
	}
	return performance



def optimiseDroplets(list_of_droplets):
	for droplet in list_of_droplets:
		stats = measurePerformance(droplet)
		if stats["memory"]>=0.75 or stats["cpu"]>=75
			#create a new droplet
		else:
			pass








def test(request):
	pass