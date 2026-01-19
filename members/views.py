from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

    return HttpResponse("<h2>試し</h2>")

def memberadd(request):
    print("memberadd関数呼び出し")
    return HttpResponse("名　〇〇　〇〇　住所：むにゃむにゃ")