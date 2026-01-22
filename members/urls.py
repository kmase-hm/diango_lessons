#　members/urls.py メンバーズアプリのurl指定

from django.urls import path
from . import views
    
    #path関数を呼び題している、urlの末尾がmembersという関数だったら

urlpatterns = [
    # urlの末尾=>関数の紐づけ
   path('', views.main, name='main'),
   path('members/', views.members, name='members'), #「members/でviewsのmembersを呼び出しますよ」
   path('members/details/<int:id>', views.details, name='details'),
   
   #path('cart_add/101/ => view.cart_add(101)), カートに商品101を追加する、というようなとき　動作名を書くことが多い　
   path('test/', views.test, name='test'),
   path('memberadd/', views.memberadd, name='memberadd'),
   path('mycareer/', views.mycareer, name='mycareer'),
   path('book/', views.books, name='book'),
   path('testing/', views.testing, name='testing'),
   path('members/mypage/',views.mypage, name='mypage'),
   path('get_post/', views.get_post, name='get_post'),
   path('nameform/', views.nameform, name='nameform'),
   path('add_member_form/', views.add_member_form, name='add_member_form'),
]
