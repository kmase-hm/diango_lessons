from django.contrib import admin
from .models import Member
    
# Register your models here.
admin.site.register(Member)

# Register your models here.
from .models import Book  # Bookモデルを読み込む
admin.site.register(Book) # 管理画面にBookを表示させる
