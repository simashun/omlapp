from django import forms
# from .models import Shouhin,Hachukanri
from .models import Shouhin

class PostForm(forms.ModelForm):

    class Meta:
        model = Shouhin
        """Shouhinモデルを使う"""
        fields = ('Shouhin_nm', 'Shouhin_cd', 'Kikaku')

class MyForm(forms.Form):
    Shouhin_nm = forms.CharField(max_length=100, required=False, label='商品名')
    Shouhin_cd = forms.IntegerField(label='商品コード')
    Kikaku = forms.CharField(max_length=100, required=False, label='規格')