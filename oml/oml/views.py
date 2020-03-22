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
    shouhin_q = request.GET.get('Shouhin_cd', None)
    # Ssername = request.GET.get('first_name', None)
    #                           Shouhin_cd
    data = {
        'is_used': Shouhin.objects.filter(Shouhin_cd__iexact=shouhin_q).exists()
        #                               Shouhin_cd.get(Shouhin_nm)
    }
    data['error_message'] = shouhin_q
    if data['is_used']:
        # data['error_message'] = 'このユーザー名は既に使用されています'
        shouhin_qnm = Shouhin.objects.get(Shouhin_cd__iexact=shouhin_q).Shouhin_nm
        data['error_message'] = shouhin_qnm
    return JsonResponse(data)