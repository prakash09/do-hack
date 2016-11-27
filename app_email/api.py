import requests	
import json
from settings import *
from views import *

def get_id():
	r1 = requests.get("https://api.digitalocean.com/v2/droplets/", headers={"Authorization" : "Bearer "+access_token})
	id1=json.loads(r1.content)['droplets'][0]['id']
	print "-------------------"
	print "Getting the id of droplet"
	print "-------------------"
	createSnapshot(id1)


def createSnapshot(droplet_id):
	print "#################"
	print "Creating Snapshot"
	print "#################"
	r1 = requests.get('https://api.digitalocean.com/v2/snapshots', headers={'Authorization': 'Bearer 4bc84c347e725c6ec6f0d42da3b3516db2e6fd9018a893988995e3a0d9aafdeb'})
	count = len(json.loads(r1.content)['snapshots'])
	r = requests.post("https://api.digitalocean.com/v2/droplets/"+str(droplet_id)+"/actions", headers={"Authorization" : "Bearer "+access_token}, data={"type":"snapshot", "name":"New Snapshot"})
	while True:
		r2 = requests.get('https://api.digitalocean.com/v2/snapshots', headers={'Authorization': 'Bearer 4bc84c347e725c6ec6f0d42da3b3516db2e6fd9018a893988995e3a0d9aafdeb'})
		if len(json.loads(r2.content)['snapshots']) > count:
			break	
	print "Droplet successfully created"
	# print json.loads(r.content)['action']['id']
	# json.loads(r.content)['action']['id']

def createDropletFromSnapshot(name="example",snapshot_id=21161926, ssh_key="4870496",region="nyc3", size="512mb"):
	print "$$$$$$$$$$$"
	print "Creating Droplet from Snapshot"
	print "$$$$$$$$$$$"
	r1=requests.get("https://api.digitalocean.com/v2/images/?private=true", headers={"Authorization" : "Bearer "+access_token})
	snapshot_id	=json.loads(r1.content)['images'][-1]['id']
	r = requests.post("https://api.digitalocean.com/v2/droplets/", headers={"Authorization" : "Bearer "+access_token, "Content-Type" : "application/json"}, data=json.dumps({"name":name, "region":region, "size":size, "image": snapshot_id, "ssh_keys":[ssh_key]}))
	r2 = requests.get("https://api.digitalocean.com/v2/droplets/", headers={"Authorization" : "Bearer "+access_token})
	print "Droplet successfully created with ID : "+str(snapshot_id)
	ip_address=json.loads(r2.content)['droplets'][-1]['networks']['v4'][0]['ip_address']
	# addServerToLoadBalancer(ip_address)


	with open('performance.sh', 'w+') as f:
		f.write("#!/bin/bash")
		f.write("vmstat -s")
	bashCommand = "scp preformance.sh root@"+ip_address+":/root/performance.sh"
	subprocess.check_output(['bash','-c', bashCommand])
	newCommand = "ssh root@"+ip+" 'chmod +x performance.sh'"
	subprocess.check_output(['bash','-c', newCommand])
	

def createDroplet(server_name,size='512mb',image='ubuntu-14-04-x64'):
	r = requests.post("https://api.digitalocean.com/v2/droplets", headers={"Authorization": "Bearer "+access_token},data={"name":"example2.com","region":"nyc3","size":"512mb","image":"ubuntu-14-04-x64","backups":False})	
	print r.status_code
	#check if the server is ready -- to-do

	#ip_address = r["ip"]

	with open('performance.sh', 'w+') as f:
		write("#!/bin/bash")
		write("vmstat -s")
	bashCommand = "scp preformance.sh root@"+ip_address+":/root/performance.sh"
	subprocess.check_output(['bash','-c', bashCommand])
	newCommand = "ssh root@"+ip+" 'chmod +x performance.sh'"
	subprocess.check_output(['bash','-c', newCommand])
	return r
def deleteDroplet(id_instance):
	print "Deleting the droplet"
	requests.delete("https://api.digitalocean.com/v2/droplets/"+str(id_instance), headers={"Authorization": "Bearer "+access_token})
	print r.status_code
	print r.content
	return r

def getIpAddress(droplet):
	r = requests.get("https://api.digitalocean.com/v2/droplets/"+droplet,headers={"Content-Type": "application/json","Authorization": "Bearer "+access_token})
	print r
	return r
def convertSnapshotToDroplet():
	r = requests.post('https://api.digitalocean.com/v2/droplets', headers={'Authorization': 'Bearer e76c1e2088c706ac7e48971fd77d4636acc806c0da47895e42705ccd107f1dc'}, data={"name":"example2.com","region":"nyc1","size":"512mb","image":"21150832"})
	print r
	return r



# def createSnapshot():

# if __name__ == "__main__":
# 	createDroplet('example2.com')	