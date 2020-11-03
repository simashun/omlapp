"""yui.models.py"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Shouhin(models.Model):
    """商品情報クラス"""
    Shouhin_cd = models.IntegerField(null=False,verbose_name='商品コード')
    Shouhin_nm = models.CharField(max_length=256,verbose_name='商品名')
    Kikaku = models.CharField(max_length=100,null=True,verbose_name='規格',blank=True)
    Siresaki_cd = models.IntegerField(null=False)
    Siresaki_nm = models.CharField(max_length=100,null=True,blank=True)
    Irisu = models.CharField(max_length=100,null=True,verbose_name='入数')
    Siretanka = models.FloatField(max_length=20,default=True)
    t_oml2 = models.ForeignKey('yui.T_oml2', on_delete=models.CASCADE, related_name='shouhins')
    # created_date = models.DateTimeField(default=timezone.now)
    def publish(self):
        """商品情報登録メソッド"""
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Shouhin_nm
    class Meta:
        verbose_name = '商品マスタ'
        verbose_name_plural = '商品マスタClass'

#class Hachukanri(models.Model):
#    """発注管理用オブジェクト"""
#    slist = models.ForeignKey(Shouhin, on_delete=models.CASCADE)
#    omllist = models.ForeignKey(T_oml2, on_delete=models.CASCADE)

    # Hachu_no = models.IntegerField(verbose_name="発注書No",null=False)
#     Iraibi = models.DateTimeField(verbose_name="依頼日")
#     Busyo = models.CharField(verbose_name="部署",max_length=20)
#     Iraisya = models.CharField(verbose_name="依頼者",max_length=20)
#     Houhou = models.CharField(verbose_name="方法",max_length=20)
#     Shukka_kokyaku = models.CharField(verbose_name="出荷顧客", max_length=20)
#     Bunrui = models.CharField(verbose_name="分類", max_length=10)
#     Shouhin_mei = models.ForeignKey(Shouhin, on_delete=models.CASCADE,verbose_name="商品名")
#     class Meta:
#         verbose_name= '発注管理T'
#         verbose_name_plural = '発注管理Class'
#     def __str__(self):
#         return self.Hachu_no

class T_oml2(models.Model):
    """発注情報クラス"""
    In_time = models.DateTimeField(verbose_name='登録年月日')
    Hachu_no = models.CharField(max_length=6,verbose_name='発注書No')
    Irai_day = models.DateTimeField(verbose_name='依頼日')
    Busyo = models.CharField(max_length=80, verbose_name='部署',null=True, blank=True)
    Irai_nm = models.CharField (max_length=80, verbose_name='依頼者', null=True)
    Houhou = models.CharField (max_length=80, verbose_name='方法', null=True, blank=True)
    Syuka_kokyaku = models.CharField (max_length=200, verbose_name='出荷顧客', null=True, blank=True)
    Hachu_nm = models.CharField (max_length=80, verbose_name='発注者')
    Bunrui = models.CharField (max_length=80, verbose_name='分類')
    # Shouhin_nm1 = models.ForeignKey(Shouhin, null=True, blank=True, on_delete=models.PROTECT)
    Shouhin_cd = models.IntegerField(verbose_name='商品CD')
    Iri_su = models.IntegerField (verbose_name='入数', null=True, blank=True)
    Case_su = models.IntegerField (verbose_name='C/S', null=True,blank=True)
    Sum_su = models.IntegerField (verbose_name='合計数量')
    Kingaku = models.IntegerField (verbose_name='金額', null=True, blank=True)
    Siresaki_cd = models.IntegerField (verbose_name='仕入先CD')
    Siresaki_nm = models.CharField (max_length=80, verbose_name='仕入先名')
    Hachu_day = models.CharField (max_length=10, verbose_name='発注日', null=True)
    Yotei_day = models.CharField (max_length=100, verbose_name='予定日', null=True, blank=True)
    Nohin_day = models.CharField (max_length=10, verbose_name='納品日', null=True, blank=True)
    Nohin_tanto_nm = models.CharField (max_length=80, verbose_name='納品担当者', null=True, blank=True)
    Tokuisaki_shuka_day = models.CharField (max_length=10, verbose_name='得意先出荷日', null=True, blank=True)
    Syoumikgn = models.CharField (max_length=10, verbose_name='賞味期限', null=True, blank=True)
    Biko = models.CharField (max_length=10000, verbose_name='備考', null=True, blank=True)
    In_tanto_cd = models.IntegerField (verbose_name='登録担当者コード', null=True)
    In_tanto_nm = models.CharField (max_length=80, verbose_name='登録担当者名', null=True)
    In_bumon_cd = models.IntegerField (verbose_name='登録部門コード', null=True)
    In_bumon_nm = models.CharField (max_length=80, verbose_name='登録部門名', null=True)
    In_tanmatu_nm = models.CharField (max_length=100, verbose_name='登録端末名', null=True)
    In_tanmatu_tanto_nm = models.CharField (max_length=80, verbose_name='登録端末担当者名', null=True)
    In_tanmatu_tanto_ip = models.CharField (max_length=1024, verbose_name='登録端末IP', null=True)
    Up_time = models.DateTimeField (verbose_name='更新年月日',default=timezone.now)
    Up_tanto_cd = models.IntegerField (verbose_name='更新担当者コード', null=True)
    Up_tanto_nm = models.CharField (max_length=80, verbose_name='更新担当者名', null=True,blank=True)
    Up_bumon_cd = models.IntegerField (verbose_name='更新部門コード', null=True,blank=True)
    Up_bumon_nm = models.CharField (max_length=80, verbose_name='更新部門名', null=True,blank=True)
    Up_tanmatu_nm = models.CharField (max_length=100, verbose_name='更新端末名', null=True,blank=True)
    Up_tanmatu_tanto_nm = models.CharField (max_length=80, verbose_name='更新端末担当者名', null=True,blank=True)
    Up_tanmatu_tanto_ip = models.CharField (max_length=1024, verbose_name='登録端末IP', null=True,blank=True)
    Del_time = models.DateTimeField (verbose_name='削除年月日', null=True,blank=True)
    Del_tanto_cd = models.IntegerField (verbose_name='削除担当者コード', null=True,blank=True)
    Del_tanto_nm = models.CharField (max_length=80, verbose_name='削除担当者名', null=True,blank=True)
    Del_bumon_cd = models.IntegerField (verbose_name='削除部門コード', null=True,blank=True)
    Del_bumon_nm = models.CharField (max_length=80, verbose_name='削除部門名', null=True,blank=True)
    Del_tanmatu_nm = models.CharField (max_length=100, verbose_name='削除端末名', null=True,blank=True)
    Del_tanmatu_tanto_nm = models.CharField (max_length=80, verbose_name='削除端末担当者名', null=True,blank=True)
    Del_tanmatu_tanto_ip = models.CharField (max_length=1024, verbose_name='削除端末IP', null=True,blank=True)
    Del_flg = models.IntegerField (verbose_name='削除フラグ', null=False, default='0',blank=True)
    Open_flg = models.IntegerField (verbose_name='公開フラグ', null=False,default='0',blank=True)
    Biken_flg = models.IntegerField (verbose_name='美健フラグ', null=False,default='0',blank=True)
    Cancel_flg = models.IntegerField (verbose_name='キャンセルフラグ', null=False,default='0',blank=True)
    def __str__(self):
        # return self.Shouhin_cd
        return self.Hachu_nm
    class Meta:
        verbose_name = '発注管理T'
        verbose_name_plural = '発注管理Class'

# class Hachukanri(models.Model):
    """発注管理用オブジェクト"""
    # slist = models.ForeignKey(Shouhin, on_delete=models.CASCADE)
    # omllist = models.ForeignKey(T_oml2, on_delete=models.CASCADE)
