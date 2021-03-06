from django.db import models
from locations.models import *

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'Category'

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=30, db_index=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        db_table = 'Firm'

    def __str__(self):
        return self.name


class Model(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория', db_index=True)
    name = models.CharField(max_length=200, verbose_name='Название', db_index=True, unique=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Product(models.Model):
    serialNumber = models.CharField(max_length=30, verbose_name='Серийный номер', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.serialNumber


class Status(models.Model):
    name = models.CharField(max_length=50,verbose_name='Статус', db_index=True)
    slug = models.SlugField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name




class Scheduler(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')


    class Meta:
        abstract = True


