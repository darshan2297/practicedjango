import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from faker import Faker
from accouts.models import topic,webpage,access

fakegen = Faker()

topics=['search','social','marketplace','news','games']

def add_topic():
    t = topic.objects.get_or_create(topic=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
     
    for entry in range(n):
        
        top = add_topic()
        
        
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #create the new webpage entry
        
        webpg = webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        
        #create a fake access record for that webpage
        
        acce_rec = access.objects.get_or_create(name=webpg,date=fake_date)[0]
        
        
if(__name__ == '__main__'):        
    print("Populating Script")
    populate(20)
    print("Populating Complete")