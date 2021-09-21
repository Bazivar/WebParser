from django.db import models

# Create your models here.
class Partnumbers(models.Model):
    #поля внутри таблицы:
    partnumber = models.CharField('Партномер (ссылка)', max_length=500, default='') #определение поля и типов данных в нём, CharField - 250 символов

    def __str__(self):
        return self.partnumber #магический метод, возврат названия объекта класса вместо его номера в админке и на сайте при вызове списка новостей

    class Meta:
        verbose_name = 'Партномер (ссылка)'
        verbose_name_plural = 'Партномеры (ссылки)'



class MassPartnumbers (models.Model):
    value_a = models.CharField('Начальная позиция', max_length=500, default='')
    value_b = models.CharField('Конечная позиция', max_length=500, default='')

    def __str__(self):
        return self.value_a,  self.value_b # магический метод, возврат названия объекта класса вместо его номера в админке и на сайте при вызове списка новостей

    class Meta:
        verbose_name = 'Начальная и конечная позиция'
        verbose_name_plural = 'Начальные и конечные позиция'