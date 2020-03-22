"""yui.views """
from django import forms
from django.utils import timezone
from django.views import generic
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse
from .models import Shouhin,T_oml2
from .forms import PostForm,MyForm
# 下記は1.11にないかも?
from django.shortcuts import redirect

# Create your views here.

# class IndexView(generic.ListView):
    # template_name = 'yui/post_list.html'
    # context_object_name = 'name_lists'
    # # context_object_nameはListViewの自動生成されるコンテキスト名を上書きする。
    # デフォルトはおそらくmodels.pyで作成したオブジェクト名となる

    # def get_queryset(self):
        # return Shouhin.objects.order_by('-created_date')[:3]
        # return Shouhin.objects.all()

def post_list(request):
    """発注管理画面メイン"""
    # name_lists = T_oml2.objects.filter(
        # Up_time__lte=timezone.now()).order_by('Up_time')
    name_lists = T_oml2.objects.order_by('Up_time')
    return render(request, 'yui/post_list.html', {'name_lists': name_lists})

def post_detail(request, pk):
    """発注情報詳細画面"""
    name2_lists = get_object_or_404(T_oml2, pk=pk)
    return render(request, 'yui/post_detail.html', {'name2_lists': name2_lists})

#def hachu_kanri(request):
#    """テスト"""
#    return render(request, 'yui/hachu_kanri.html')

def post_new(request):
    """入力フォームテスト"""
    if request.method == "POST":
        """POSTが定義されている場合"""
        # form = PostForm(request.POST)
        form = MyForm(request.POST)
        if form.is_valid():

            """is_valid → 必須チェック、不正値チェック"""
            post = form.save(commit=False)
            """すぐには保存しない"""
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('/yui/')
            return redirect('post_detail', pk=post.pk)
    else:
            """フォーム初期状態の場合"""
            # form = PostForm()
            initial_dict = {
                'In_time' : timezone.now,
                'Irai_day' : timezone.now,
            }
            form = MyForm(initial=initial_dict)
    return render(request, 'yui/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(T_oml2, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=post)
        # form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # form = PostForm(instance=post)
        form = MyForm(instance=post)
    return render(request, 'yui/edit.html', {'form': form})

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