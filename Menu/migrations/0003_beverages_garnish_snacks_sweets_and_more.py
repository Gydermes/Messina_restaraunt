# Generated by Django 4.1.1 on 2022-09-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_second_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dishes', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Garnish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dishes', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Snacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dishes', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_dishes', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='first_course',
            name='name_of_dishes',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='second_course',
            name='name_of_dishes',
            field=models.CharField(max_length=100),
        ),
    ]