from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Book

# Create your views here.
# パスと連動した関数を書く

    
def members(request): #引数は習慣としてrequestを入れる。
    print("menbers呼び出し")
    # htmlファイルを探す
    template = loader.get_template('myfirst.html')
    # htmlファイルをデータ化して返信する
    return HttpResponse(template.render())

def test(request):
    print("test関数呼び出し")
    ans = 12*2
    str = f'answer = {ans}'
    return HttpResponse(str)

def memberadd(request):
    print("memberadd関数呼び出し")
    return HttpResponse("名：〇〇　〇〇　住所：むにゃむにゃ")

def mycareer(request):
    print("mycareer関数呼び出し")
    return  render(request, 'mycareer.html')

def members(request):
   mymembers = Member.objects.all().values()
   print(mymembers)
   template = loader.get_template('all_members.html')
  
   #HTMLに渡す辞書データ
   context = {
      'mymembers': mymembers,
      'myname':'Taro suzuki' 
   }
   return HttpResponse(template.render(context, request)) 
   
    #個人データを表示
def details(request, id):
    #idを検索して1件のレコードを取得
   mymember = Member.objects.get(id=id)
   template = loader.get_template('details.html')
   context = {
      'mymember': mymember,
   }
   return HttpResponse(template.render(context, request))

def books(request):
   books = Book.objects.all().values()
   print(books)
   template = loader.get_template('books.html')

   #HTMLに渡す辞書データ
   context = {
      'books': books,
   }
   return HttpResponse(template.render(context, request)) 