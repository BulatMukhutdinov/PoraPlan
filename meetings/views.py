from django.shortcuts import render, redirect, render_to_response


# Create your views here.


def meetings(request):
    return render(request, 'meetings.html')
