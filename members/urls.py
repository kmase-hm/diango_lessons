#　members/urls.py メンバーズアプリのurl指定

from django.urls import path
from . import views
    
    #path関数を呼び題している、urlの末尾がmembersという関数だったら

urlpatterns = [
    # urlの末尾=>関数の紐づけ
   path('members/', views.members, name='members'),
   path('test/', views.test, name='test'),
   path('memberadd/', views.memberadd, name='memberadd'),
]