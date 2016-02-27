import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100) # имя товара
    price = models.CharField(max_length=100) # цена товара
    description = models.TextField()
    comment = models.TextField()
    # author = models.ForeignKey('auth.User') # ссылка на другую модель
    # title = models.CharField(max_length=200) # тескстовое поле с огранич кол-вом записей
    # text = models.TextField() # с неогранич кол-вом записей

    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    
    '''def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title'''