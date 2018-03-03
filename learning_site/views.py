from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms


def hello_world(request):
    return render(request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),#subject line
                form.cleaned_data['suggestion'], #body of email
                '{name} <{email}>'.format(**form.cleaned_data), #email its from (will use dict keys to fill out the 'name/email'
                ['bez@yahoo.com'] #where it sends mail
            )
            messages.add_message(request, messages.SUCCESS, #able to put in flash messages
                                 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})
def html_page(request):
    return render(request, 'admission.html')