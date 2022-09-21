from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Menu


def menu(request):
    return render(request, 'Menu/menu.html')


def first_course(request):
    course = Menu.objects.all()
    res = []
    for item in course:
        res += f'{item.Food_classification} {item.name_of_dishes} {item.price} '

    return HttpResponse(res)


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