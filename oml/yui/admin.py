from django.contrib import admin
from .models import Shouhin,T_oml2
# Register your models here.

admin.site.register(Shouhin)
# admin.site.register(Hachukanri)
class ShouhinAdmin(admin.ModelAdmin):
    fields = ['In_time', 'Hachu_no', 'Irai_day', 'Busyo', 'Irai_nm', 'Houhou', 'Syuka_kokyaku', 'Hachu_nm', 'Bunrui', 'Shouhin_cd', 'Iri_su', 'Case_su', 'Sum_su', 'Kingaku', 'Siresaki_cd', 'Siresaki_nm', 'Hachu_day', 'Yotei_day', 'Nohin_day', 'Nohin_tanto_nm', 'Tokuisaki_shuka_day', 'Syoumikgn', 'Biko', 'In_tanto_cd', 'In_tanto_nm', 'In_bumon_cd', 'In_bumon_nm', 'In_tanmatu_nm', 'In_tanmatu_tanto_nm', 'In_tanmatu_tanto_ip', 'Up_time', 'Up_tanto_cd', 'Up_tanto_nm', 'Up_bumon_cd', 'Up_bumon_nm', 'Up_tanmatu_nm', 'Up_tanmatu_tanto_nm', 'Up_tanmatu_tanto_ip', 'Del_time', 'Del_tanto_cd', 'Del_tanto_nm', 'Del_bumon_cd', 'Del_bumon_nm', 'Del_tanmatu_nm', 'Del_tanmatu_tanto_nm', 'Del_tanmatu_tanto_ip', 'Del_flg', 'Open_flg', 'Biken_flg', 'Cancel_flg']
    list_display = ['ProductName', 'In_time', 'Hachu_no', 'Irai_day', 'Busyo', 'Irai_nm', 'Houhou', 'Syuka_kokyaku', 'Hachu_nm', 'Bunrui', 'Shouhin_nm1', 'Shouhin_cd', 'Iri_su', 'Case_su', 'Sum_su', 'Kingaku', 'Siresaki_cd', 'Siresaki_nm', 'Hachu_day', 'Yotei_day', 'Nohin_day', 'Nohin_tanto_nm', 'Tokuisaki_shuka_day', 'Syoumikgn', 'Biko', 'In_tanto_cd', 'In_tanto_nm', 'In_bumon_cd', 'In_bumon_nm', 'In_tanmatu_nm', 'In_tanmatu_tanto_nm', 'In_tanmatu_tanto_ip', 'Up_time', 'Up_tanto_cd', 'Up_tanto_nm', 'Up_bumon_cd', 'Up_bumon_nm', 'Up_tanmatu_nm', 'Up_tanmatu_tanto_nm', 'Up_tanmatu_tanto_ip', 'Del_time', 'Del_tanto_cd', 'Del_tanto_nm', 'Del_bumon_cd', 'Del_bumon_nm', 'Del_tanmatu_nm', 'Del_tanmatu_tanto_nm', 'Del_tanmatu_tanto_ip', 'Del_flg', 'Open_flg', 'Biken_flg', 'Cancel_flg']
    def ProductName(self,obj):
        return str()
    ProductName.short_description = "商品名"
admin.site.register(T_oml2,ShouhinAdmin)