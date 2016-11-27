import requests	
import json
from app_email.settings import *
def createDroplet(server_name,size='512mb',image='ubuntu-14-04-x64'):
	r = requests.post("https://api.digitalocean.com/v2/droplets", headers={"Authorization": "Bearer "+access_token},data=({"name":"example2.com","region":"nyc3","size":"512mb","image":"ubuntu-14-04-x64","backups":False}))	print r.status_code
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

if __name__ == "__main__":
	createDroplet('example2.com')	