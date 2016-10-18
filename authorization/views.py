# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def sign_up(request):
    return render(request, 'sign_up.html')


def error(request):
    return render(request, 'error.html')


def profile(request):
    return render(request, 'profile.html')


def sign_up_process(request):
    post = request.POST
    if not user_exists(post['email']):
        create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/error")


def sign_in(request):
    if 'next' in request.GET:
        request.next_page = request.GET['next']
    return render(request, 'sign_in.html')


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def auth_and_login(request, onsuccess='/', onfail='sign_in'):
    next_page = onsuccess
    if 'next' in request.GET:
        next_page = request.POST['next']
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        request.session['login_message'] = 'Enter the username and password correctly'
        return redirect(onfail)


def log_out(request):
    logout(request)
    return redirect('/authorization/sign_in')


def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@login_required(login_url='/authorization/login/')
def secured(request):
    return render_to_response("secure.html")
