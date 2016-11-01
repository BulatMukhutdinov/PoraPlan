from django.views.generic import UpdateView
from account.models import Account
from django.core.urlresolvers import reverse_lazy


class AccountView(UpdateView):
    model = Account
    success_url = reverse_lazy('account_view')
    fields = ['avatar', 'birthday', 'company', 'position']

    def get_object(self):
        instance, created = Account.objects.get_or_create(user=self.request.user, defaults={'user': self.request.user})
        instance.save()
        return instance
