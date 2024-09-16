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