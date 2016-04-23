import facebook   
import itertools
import json
import re
import requests
import csv

access_token = "EAACEdEose0cBACVtkzfbfRinu0kWYi2QaJtPczxGbu6WNAkVtdlTJv3Rz9BtZCeJGkjnN5rqga4pUsZAtameyvEJfLREYDJBlrrfIEn0H4t2pYO54uaW7intAZCJyUvlWmptudZCgN888ITl2xxr8aUEC5aRDYca9evESWPuWQZDZD"
graph = facebook.GraphAPI(access_token)

profile = graph.get_object("me") 
family=graph.get_object("me/family")
famname=[]
for every in family['data']:
	famname.append([every['name'],every['relationship']])	
print famname
friends=graph.get_object("me/friends")  
#print family
#print friends
fdata = graph.get_connections(profile['id'], 'friends')
#print fdata
girls=[]
townbudd=[]
for data in fdata['data']:
    fulldet=graph.get_object(id=data['id'])
    #print fulldet
    if(fulldet['gender']=="male"):			#create file of friends who are girls
    	girls.append([data['name'],data['id']])
    #if(fulldet['hometown']==profile['hometown']):# group of hometown buddies
    	#townbudd.append([data['name'],data['id']])
   
with open('Family.csv', 'wb') as fp:	#group of family
        file = csv.writer(fp, delimiter=',')
        file.writerow(['name','id'])
        file.writerows(famname)
with open('Girls.csv', 'wb') as fp:
        file = csv.writer(fp, delimiter=',')
        file.writerow(['name','id'])
        file.writerows(girls)
#with open('Home.csv', 'wb') as fp:
       # file = csv.writer(fp, delimiter=',')
        #file.writerow(['name','id'])
        #file.writerows(townbudd)

    
    


