from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()

        context = dict(name='Henrique Bastos', cpf='12345678901',
                       email='henrique@bastos.net', phone='21-99618-6180')

        body = render_to_string('subscriptions/subscription_email.txt',
                                form.cleaned_data)

        mail.send_mail('Confirmação de inscrição',
                       body,
                       'contato@eventex.com.br',
                       ['contato@eventex.com.br', form.cleaned_data['email']])

        return HttpResponseRedirect('/inscricao/')

    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)

