from django.contrib import admin

# Register your models here.

from .models import Post, convertRate

admin.site.register(Post)
admin.site.register(convertRate)