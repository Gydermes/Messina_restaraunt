# Generated by Django 4.1.1 on 2022-09-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Second_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dishes', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
