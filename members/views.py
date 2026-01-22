from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Book
from django.shortcuts import redirect, render
from .forms import MemberForm


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

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

def testing(request):
   template = loader.get_template('template.html')
 
   context = {
         # 辞書
         # {{キー名}}でHTMLへ手渡しできる
          'firstname': 'Yukari',
          'price': [12000, 50000],
          'greeting':3,
          'fruits':['apple','banana','cherry','dragonfruit'],
    }
   
   return HttpResponse(template.render(context, request))

def mypage(request):
   template = loader.get_template('mypage.html')
   context = {
      'apps':['夜活支援','旅日記','とりあえず家計簿','落書き長']
   }
   return HttpResponse(template.render(context, request))

# Django のビュー（画面の処理を書く場所）
from django.shortcuts import render

def get_post(request):
    # message という変数を初期化（最初は何も入れない）
    message = "GET"  # Noneを"GET"に★

   #  # ブラウザから送られてきた HTTP メソッドを判別　★コメントアウト
   #  if request.method == "GET":
   #      # GET のときに行う処理
   #      # ページを開いたとき（リンクをクリックしたとき）など
   #      message = "GET"

    if request.method == "POST":  #elifをifにした　★
        # POST のときに行う処理
        # フォームを送信したときなど
        message = "POST"

    # テンプレートに渡すデータを辞書でまとめる
    context = {'message': message}

    # get_post.html を表示し、context の内容をテンプレートに渡す
    return render(request, 'get_post.html', context)


def nameform(request):
    display_name = None
    display_email = None
    # フォームに入力されたデータの取得
    if request.method == 'POST':
        display_name = request.POST.get('your_name')
        display_email = request.POST.get('your_email')
    context = {
        'display_name': display_name,
        'display_email': display_email,
    }

    return render(request, 'nameform.html', context)

def add_member_form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid(): # 入力内容が正しいか自動チェック
            # クリーニングされたデータを取得して保存
            data = form.cleaned_data
            Member.objects.create(**data) # ←備考説明あり
            return redirect('members')
    else:
        form = MemberForm() # 空のフォームを作成
    
    return render(request, 'add_form.html', {'form': form})