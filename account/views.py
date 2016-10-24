from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from account.models import Account
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render


#
# class AccountPage(DetailView):
#     model = Account
#
#     def get_object(self):
#         return get_object_or_404(Account, pk=request.session['user_id'])


def account(request):
    return render(request, 'account.html')