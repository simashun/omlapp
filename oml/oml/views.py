"""oml.views """
from django import forms
from django.utils import timezone
from django.views import generic
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse
from yui.models import Shouhin,T_oml2
from django.shortcuts import redirect

def validate_username(request):
    """商品名自動補完メソッド(jQuery)"""
    shouhin_q = request.GET.get('Shouhin_cd', None)
    data = {
        'is_used': Shouhin.objects.filter(Shouhin_cd__iexact=shouhin_q).exists()
    }
    data['error_message'] = shouhin_q
    if data['is_used']:
        shouhin_qnm = Shouhin.objects.get(Shouhin_cd__iexact=shouhin_q).Shouhin_nm
        data['error_message'] = shouhin_qnm
    return JsonResponse(data)