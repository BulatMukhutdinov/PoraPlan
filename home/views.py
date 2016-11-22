from django.shortcuts import render


# Create your views here.
#@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
