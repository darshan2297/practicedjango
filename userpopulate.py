import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice.settings')

import django
django.setup()

#fake operation

from faker import Faker
from accouts.models import user

fakeobj = Faker()

def populate(n=0):
    
    for entry in range(n):

        fake_fname = fakeobj.first_name()
        fake_lname = fakeobj.last_name()
        fake_email = fakeobj.email()

        users = user.objects.get_or_create(fname=fake_fname,lname=fake_lname,email=fake_email)[0]
        users.save()

if(__name__ == '__main__'):
    print("Poulate scripting")
    populate(20)
    print("Poulate Complete")
    


