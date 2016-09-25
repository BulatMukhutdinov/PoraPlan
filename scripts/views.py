# Create your views here.


from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def root_index(request):
    return redirect('/app')


def index(request):
    template = loader.get_template('scripts/startpage.html')
    return HttpResponse(template.render(request))


    #template = loader.get_template('scripts/index.html')
    #if request.user.is_authenticated():
    #    context = {
    #        'user':request.user
    #    }
    #    return HttpResponse(template.render(context, request))
    #else:
    #    return redirect('/app/login')

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def login2(request):
    template = loader.get_template('scripts/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)


def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user


def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/login/")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@login_required(login_url='/login/')
def secured(request):
    return render_to_response("secure.html")