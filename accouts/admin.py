from django.contrib import admin
from .models import topic,webpage,access,user,profile,UserprofileInfo


# Register your models here.

admin.site.register(topic)
admin.site.register(webpage)
admin.site.register(access)
admin.site.register(user)
admin.site.register(profile)
admin.site.register(UserprofileInfo)