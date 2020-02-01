from django.urls import path
from django.conf.urls import url
from testreglog import views

app_name = 'testreglog'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.user_login,name='user_login'),
    path('logout',views.user_logout,name='user_logout')
]
