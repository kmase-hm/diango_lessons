from django import forms

# フォームの形を定義（モデルとは独立）
class MemberForm(forms.Form):
    firstname = forms.CharField(label='名', max_length=255)
    lastname = forms.CharField(label='姓', max_length=255)
    phone = forms.IntegerField(label='電話番号', required=False)
    joined_date = forms.DateField(label='入会日', widget=forms.SelectDateWidget)
