

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms, udemyOOP, models
from django.views.generic import View, TemplateView, ListView, DetailView


class SpeechHomeView(TemplateView):
    template_name = 'jobs/speechHome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["another_key"] = 'value to giv to the template'
        return context

class HelloWorldView(View):

    def get(self, request):
        return HttpResponse('string')


def speech(request):
    form = forms.NoteForm()
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('jobs:speech'))
    return render(request, 'jobs/speech.html', {'form': form})


# def patient_list(request):
#     patients = models.Patient.objects.all()
#     return render(request, 'jobs/patient_list.html',  {'patients': patients})
class PatientListView(ListView):
    context_object_name = "patients"
    model = models.Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["another_key"] = 'value to giv to the template'
        return context

class PatientDetailView(DetailView):
    model = models.Patient



class Car:
    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        return ('Hatchback is: {}'.format(self.carFare['Hatchback']) +
                '---Sedan is: {}'.format(self.carFare['Sedan']) +
                '---SUV is: {}'.format(self.carFare['SUV'])
                )
        # print("Cost per day: ")
        # print("Hatchback: $",self.carFare['Hatchback'])
        # print("Sedan: $", self.carFare['Sedan'])
        # print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[typeOfCar] * numberOfDays
# car = Car()
# while True:
#     print("Enter 1 to display the fare details")
#     print("Enter 2 to rent a car")
#     print("Enter 3 to exit")
#     userChoice = (int(input()))
#     if userChoice is 1:
#         car.displayFareDetails()
#     elif userChoice is 2:
#         print("Enter the type of car you would like to borrow")
#         typeOfCar = input()
#         print("Enter the number of days you would like to borrow the car")
#         numberOfDays = int(input())
#         fare = car.calculateFare(typeOfCar, numberOfDays)
#         print("Total payable amount: $",fare)
#         print("Thank you!")
#     elif userChoice is 3:
#         quit()


def udemy(request):
    car = Car()
    x1 = '''#     ("Enter 1 to display the fare details")
            #     ("Enter 2 to rent a car")
            #     ("Enter 3 to exit")'''
    x2 = 1
    form = request.META.get('QUERY_STRING')
    reply = form[7:]
    if reply == '1':
        reply = car.displayFareDetails()
        reply = str(reply)
    elif reply == '2':
        pass
    elif reply == '3':
        pass

    return render(request, 'jobs/udemy.html', {'reply': reply, 'x':x1})


