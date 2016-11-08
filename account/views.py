from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.views.generic import UpdateView,DetailView
from account.models import Account
from account.form import AccountForm
from django.core.urlresolvers import reverse_lazy


class AccountUpdate(UpdateView):
    model = Account
    success_url = reverse_lazy('account_detail')
    template_name = "account_update.html"
    fields = ['avatar','company', 'position', 'birthday','phone','country','city','website']

    def get_object(self):
        instance, created = Account.objects.get_or_create(user=self.request.user, defaults={'user': self.request.user})
        instance.save()
        return instance

    def form_valid(self, form):
        form.save()
        return super(AccountUpdate, self).form_valid(form)

class AccountDetail(UpdateView):
    model = Account
    template_name = "account_detail.html"
    fields = ['avatar','company', 'position', 'birthday','phone','country','city','website']

    def get_object(self):
        instance, created = Account.objects.get_or_create(user=self.request.user, defaults={'user': self.request.user})
        instance.save()
        return instance
    def form_valid(self, form):
        form.save()
        return super(AccountDetail, self).form_valid(form)
