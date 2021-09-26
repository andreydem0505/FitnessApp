from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Таблица информации о пользователе, связана с ним связью "один к одному"
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    weight = models.IntegerField('Вес')
    height = models.IntegerField('Рост')
    birthdate = models.DateField('Дата рождения')
    gender = models.CharField('Пол', choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)
    norm = models.IntegerField('Норма калорий')

    def __str__(self):
        return self.user.username


# Таблица приёма пищи
class Ingestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    food = models.CharField('Еда', max_length=200)
    calories = models.IntegerField('Калории')
    date = models.DateField('Дата', default=datetime.now())

    def __str__(self):
        return self.food
