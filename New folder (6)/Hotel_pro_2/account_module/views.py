from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def login_page(request: HttpRequest):
    return render(request, 'account_module/login_page.html')