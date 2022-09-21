from django.db import models


class First_course(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}\n'


class Second_course(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'


class Sweets(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'


class Garnish(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'


class Beverages(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'


class Snacks(models.Model):
    name_of_dishes = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'

