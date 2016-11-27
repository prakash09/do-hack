from django.shortcuts import render
import subprocess
from api import *
import threading
# Create your views here.
load_balancer_exists=False
counter=0
instance_size = "512mb"
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
	print "optimising the server"
	sum_memory = 0
	min_stat = -1
	min_val = 10000
	for droplet in list_of_droplets:

		stats = measurePerformance(droplet)
		print "Stats are :" +stats["memory"]
		sum_memory+=stats["memory"]
		if min_val > stats["memory"]:
			min_val = stats["memory"]
			min_stat = droplet
	sum_memory = 100
	if sum_memory/len(list_of_droplets)>=0.75:
		if not load_balancer_exists:
			print "creating the load balancer"
			createDropletFromSnapshot(name="example"+counter+".com",size=instance_size)
		else:
			print "creating the droplet"
			get_id()
			createDropletFromSnapshot(name="example"+counter+".com",size=instance_size)
			counter+=1
		print r
		return r
	elif sum_memory/len(list_of_droplets)<=0.25:
		print "deleting the droplet due to low traffic"
		r = deleteDroplet(min_stat)
		print r
		min_stat = -1
		min_val = 10000
		return r


# def set_interval(func,list_of_droplets ,sec):
#     def func_wrapper():
#         set_interval(func,list_of_droplets ,sec)
#         print "hitting the ip addresses"
#         print func(list_of_droplets)
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

def maintainDroplets():
	# list_of_droplets = requests.get('http://localhost:80/upstream_conf?upstream=backend')
	# print list_of_droplets
	list_of_droplets = ["104.131.5.143", "159.203.130.164", "138.197.27.13","138.197.26.225","104.236.215.110"]
	optimiseDroplets(list_of_droplets)

def addServerToLoadBalancer(server_ip):
	requests.get('http://localhost:80/upstream_conf?add=&upstream=backend&server='+server_ip)

def start_loading():
	print "Size of the instance: "
	instance_size = str(raw_input())

	print "Do you want it to be automatic or you want it to be notified?"
	maintainDroplets()

if __name__ == "__main__":
	start_loading()