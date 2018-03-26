
from django.shortcuts import get_object_or_404, render
from . import models



# Create your views here.
def trial(request):
    return render(request, 'uiux/trial.html')



