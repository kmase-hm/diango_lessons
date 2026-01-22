### 何か説明のためのフォルダやファイルを置いておきたいとき
プロジェクトのフォルダ直下に何かフォルダやファイルを作ってOK、特に邪魔しない。




# Django のビュー（画面の処理を書く場所）
from django.shortcuts import render

def get_post(request):
    # message という変数を初期化（最初は何も入れない）
    message = None

    # ブラウザから送られてきた HTTP メソッドを判別
    if request.method == "GET":
        # GET のときに行う処理
        # ページを開いたとき（リンクをクリックしたとき）など
        message = "GET"

    elif request.method == "POST":
        # POST のときに行う処理
        # フォームを送信したときなど
        message = "POST"

    # テンプレートに渡すデータを辞書でまとめる
    context = {'message': message}

    # get_post.html を表示し、context の内容をテンプレートに渡す
    return render(request, 'get_post.html', context)


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