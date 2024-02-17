from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Computer(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    computer_qty = models.IntegerField()
    configuration = models.TextField(max_length=1000, blank=True, default='The configuration is not filled in')
    details = models.TextField(blank=True, default='A detailed description has not yet been added')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    create_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True, verbose_name="Photo")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Компьютеры'
        verbose_name = 'Компьютер'
        ordering = ['-id']