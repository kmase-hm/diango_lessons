# members フォルダの下に/models.py がもともと作られる
# テーブルの作成（モデル）
from django.db import models

#class名がテーブル名　SQLじゃなくてクラスで書くのが主流になってる
class Member(models.Model):
   #列名＝データ型クラス（VARCHAR（255））
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
   #row = models.関数　を使ったりできる　modelsモジュールにいろいろ入っている
   phone = models.IntegerField(null = True)  #nullを許容する
   joined_date = models.DateField(null = True)
   #ここのnull = Trueは非常に大事

   # オブジェクト（データ）の文字列表現を返す
   def __str__(self):   
      return f"{self.firstname} {self.lastname}";

class Book(models.Model):
    #列名＝データ型クラス（VARCHAR（255））
   title = models.CharField(max_length=255)
   author = models.CharField(max_length=255)
