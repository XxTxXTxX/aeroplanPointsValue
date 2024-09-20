from django.db import models
from django.utils import timezone

# Create your models here.


# content page

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class recordUsage(models.Model):
    user_id = models.BigIntegerField(name='用户id')
    useTime = models.BigIntegerField(name='用户使用次数', default=0)
    lastTime = models.DateTimeField(name='用户最后使用时间', auto_now_add=True)

class convertRate(models.Model):
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    base_fare = models.BigIntegerField(verbose_name='base_fare', default=0)
    date = models.DateField(name='date', null=True, blank=True)
    points = models.BigIntegerField(name='points')
    cash = models.BigIntegerField(name='cash')
    result = models.DecimalField(name='convertRate', max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"Conversion from {self.departure} to {self.arrival}"
    