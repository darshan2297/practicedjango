from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'firstapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('display',views.display,name='display'),
    path('form',views.form,name='form'),
    path('success',views.success,name='success'),
    path('login',views.login),
    path('logout',views.logout,name='logout')
    #path('sendmail',views.simplesendemail,name='sendemail')
    # url(r'^(?P<slug>[\w-]+)/$',views.slug,name='slug'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()