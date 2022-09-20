from django.shortcuts import render

def login(request):
    context = {

    }
    return render(request,'web/login.html',context)


def register(request):
    context = {

    }
    return render(request,'web/register.html',context)


def forgot_password(request):
    context = {

    }
    return render(request,'web/forgot-password.html',context)


def profile(request):
    context = {

    }
    return render(request,'web/profile.html',context)


def settings(request):
    context = {

    }
    return render(request,'web/settings.html',context)


def index(request):
    context = {

    }
    return render(request,'web/index.html',context)