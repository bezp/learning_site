from django.shortcuts import render
from . import forms
# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from xml.dom import minidom
from collections import namedtuple
import requests

def speech(request):
    form = forms.NoteForm()
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jobs:speech'))


    return render(request, 'jobs/speech.html', {'form': form})





