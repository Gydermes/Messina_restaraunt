from django.db import models



class Food_classification(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.title} '



class Menu(models.Model):
    name_of_dishes = models.CharField(max_length=40)
    price = models.CharField(max_length=10)
    Food_classification = models.ForeignKey(Food_classification, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_of_dishes}  {self.price}'



