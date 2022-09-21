from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import First_course, Second_course, Snacks, Garnish, Sweets, Beverages


def menu(request):
    return render(request, 'Menu/menu.html')


def first_course(request):
    course = First_course.objects.all()
    res = []
    for item in course:
        res += f' \n{item.name_of_dishes} "{item.price}\n"'
    return HttpResponse(res)


def second_course(request):
    course = Second_course.objects.all()
    res = []
    for item in course:
        res += f' {item.name_of_dishes} "{item.price}"'
    return HttpResponse(res)


def snacks(request):
    course = Snacks.objects.all()
    res = []
    for item in course:
        res += f' {item.name_of_dishes} "{item.price}"'
    return HttpResponse(res)


def garnish(request):
    course = Garnish.objects.all()
    res = []
    for item in course:
        res += f' {item.name_of_dishes} "{item.price}"'
    return HttpResponse(res)


def sweets(request):
    course = Sweets.objects.all()
    res = []
    for item in course:
        res += f' {item.name_of_dishes} "{item.price}"'
    return HttpResponse(res)


def beverages(request):
    course = Beverages.objects.all()
    res = []
    for item in course:
        res += f' {item.name_of_dishes} "{item.price}"'
    return HttpResponse(res)