from django.shortcuts import HttpResponse
from django.shortcuts import render


def menu(request):
    return render(request, 'Menu/menu.html')


def first_course(request):
    return HttpResponse('first_course')


def second_course(request):
    return HttpResponse('second_course')


def snacks(request):
    return HttpResponse('snacks')


def garnish(request):
    return HttpResponse('garnish')


def sweets(request):
    return HttpResponse('sweets')


def beverages(request):
    return HttpResponse('beverages')