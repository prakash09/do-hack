import requests	
import json
from settings import *
def createDroplet(server_name,size='512mb',image='ubuntu-14-04-x64'):

	r = requests.post("https://api.digitalocean.com/v2/droplets", headers={"Authorization": "Bearer "+access_token},data=({"name":"example2.com","region":"nyc3","size":"512mb","image":"ubuntu-14-04-x64","backups":False}))
	print r.status_code
	print r.content
def deleteDroplet(id_instance):
	requests.delete("https://api.digitalocean.com/v2/droplets/"+str(id_instance), headers={"Authorization": "Bearer "+access_token})
	print r.status_code
	print r.content

def createSnapshot():

if __name__ == "__main__":
	createDroplet('example2.com')	