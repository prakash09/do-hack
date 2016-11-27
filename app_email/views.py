from django.shortcuts import render
import subprocess
from api import *
import threading
# Create your views here.
load_balancer_exists=False
counter=0
def measurePerformance(ip_address):
	bashCommand="ssh root@"+ip_address+" './performance.sh'"
	output = subprocess.check_output(['bash','-c', bashCommand])
	x = output.split('\n')
	total_memory = int(x[0].split()[0])
	used_memory = int(x[1].split()[0])
	memory_ratio = used_memory*1.0/total_memory
	performance = {
		"memory":memory_ratio
	}
	return performance



def optimiseDroplets(list_of_droplets):
	sum_memory = 0
	min_stat = -1
	min_val = 10000
	for droplet in list_of_droplets:
		stats = measurePerformance(droplet)
		sum_memory+=stats["memory"]
		if min_val > stats["memory"]:
			min_val = stats["memory"]
			min_stat = droplet
	if sum_memory/len(list_of_droplets)>=0.75
		if not load_balancer_exists:
			createLoadBalancer()
		else:
			r = createDroplet("example"+counter+".com")
			counter+=1
		print r
		return r
	elif sum_memory/len(list_of_droplets)<=0.25:
		r = deleteDroplet(min_stat)
		print r
		min_stat = -1
		min_val = 10000
		return r


def set_interval(func,list_of_droplets ,sec):
    def func_wrapper():
        set_interval(func,list_of_droplets ,sec)
        print func(list_of_droplets)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def maintainDroplets():
	set_interval(optimiseDroplets,list_of_droplets,30)

def addServerToLoadBalancer(server_ip):
	requests.get('http://localhost:80/upstream_conf?add=&upstream=backend&server='+server_ip)

def start_loading():
	maintainDroplets()