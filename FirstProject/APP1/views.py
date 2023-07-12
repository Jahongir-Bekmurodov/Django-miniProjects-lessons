from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def birortanom(request):
    title = "Asosiy sahifa"
    info = "Head of BOTTLE"
    return render(request, 'birortanom.html',
                  {'title': title,
                   'info': info})
    # return HttpResponse("Bu yerda ma'noli so'z bo'lishi mumkin edi")
def matnnom(request):
    return render(request, )