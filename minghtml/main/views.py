from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse
from main.models import Article
from main.forms import ArticleForm

def main(request):
    return render(request,'main/main.html')

def cyut(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'main/cyut.html', context)

def version(request):
    return render(request,'main/version.html')

def connection(request):
    return render(request,'main/connection.html')

def computer(request):
    return render(request,'main/computer.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth
