from tkinter import CASCADE
from django.db import models

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=40,)
    etaj = models.IntegerField()
    hujra = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'


class Calendar(models.Model):
    MONTH_CHOICES = [
        ("January","Январь"),
        ("February","Февраль"),
        ("March","Март"),
        ("April","Апрель"),
        ("May","Май"),
        ("June","Июнь"),
        ("July","Июль"),
        ("August","Август"),
        ("September","Сентябрь"),
        ("October","Октябрь"),
        ("November","Ноябрь"),
        ("December","Декабрь")
    ]
    YEAR_CHOICE = [
        ("22", "2022"),
        ("23", "2023"),
        ("24", "2024"),
        ("25", "2025"),
        ("26", "2026"),
    ]
    pardoxt = models.IntegerField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES, default="Номуайян")
    date = models.DateTimeField(auto_now_add=True)
    year = models.CharField(max_length=3, choices=YEAR_CHOICE, default=2022)
    spisok = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.month

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платёжи'