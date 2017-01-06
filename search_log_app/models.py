from django.db import models

class Response(models.Model):
    title = models.GenericIPAddressField(verbose_name='TITLE')
    number = models.IntegerField(verbose_name='NUMBER', max_length=4)
    name = models.CharField(verbose_name='NAME', max_length=50)
    date = models.CharField(verbose_name='DATE', max_length=10)
    time = models.CharField(verbose_name='TIME', max_length=10)
    text = models.TextField(verbose_name='TEXT')
    html = models.CharField(verbose_name='HTML', max_length=30)
