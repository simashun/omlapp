from django import forms
# from .models import Shouhin,Hachukanri
from .models import Shouhin,T_oml2

class PostForm(forms.ModelForm):
    pass
    class Meta:
        model = Shouhin
        """Shouhinモデルを使う"""
        """既存行編集時に参照"""
        fields = ('Shouhin_nm', 'Shouhin_cd', 'Kikaku','Irisu')

class MyForm(forms.ModelForm):
    """新規登録時のフォーム"""
    Hachu_no = forms.CharField(max_length='6',label='発注書No')
    In_time = forms.DateField(label='登録年月日')
    Irai_day = forms.DateField (label='依頼日')
    Busyo = forms.CharField(max_length=80,label='部署')
    Irai_nm = forms.CharField (max_length=80, label='依頼者')
    Houhou = forms.CharField (max_length=80, label='方法' )
    Syuka_kokyaku = forms.CharField (max_length=200, label='出荷顧客')
    Hachu_nm = forms.CharField (max_length=80, label='発注者')
    Bunrui = forms.CharField (max_length=80, label='分類')
    Kikaku = forms.CharField(max_length=20,label="規格")
    Shouhin_cd = forms.IntegerField(label="商品CD")
    Iri_su = forms.IntegerField (label='入数')
    Case_su = forms.IntegerField (label='C/S')
    Sum_su = forms.IntegerField (label='合計数量')
    Kingaku = forms.IntegerField (label='金額')
    Siresaki_cd = forms.IntegerField (label='仕入先CD')
    Siresaki_nm = forms.CharField (max_length=80, label='仕入先名')
    Hachu_day = forms.CharField (max_length=10, label='発注日')
    Yotei_day = forms.CharField (max_length=100, label='予定日')
    Nohin_day = forms.CharField (max_length=10, label='納品日')
    Nohin_tanto_nm = forms.CharField (max_length=80, label='荷受者')
    Tokuisaki_shuka_day = forms.CharField (max_length=10, label='得意先出荷日')
    Biko = forms.CharField (max_length=10000, label='備考')

    class Meta:
        model = T_oml2
        fields = ('Hachu_no','In_time','Irai_day','Busyo','Irai_nm','Houhou','Syuka_kokyaku','Hachu_nm','Bunrui','Kikaku','Shouhin_cd','Iri_su','Case_su','Sum_su','Kingaku','Siresaki_cd','Hachu_day','Yotei_day','Nohin_day','Nohin_tanto_nm','Tokuisaki_shuka_day','Biko')