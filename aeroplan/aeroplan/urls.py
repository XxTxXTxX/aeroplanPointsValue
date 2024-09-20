"""
URL configuration for aeroplan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
import bbs.views
from article.views import index

admin.site.site_header = "登录测试用"
admin.site.site_title = 'Aeroplan Points Rate Checker'
admin.site.index_title = 'Admin page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path("", index, name="index"),
    path('bbs/posts', views.get_posts, name='get_posts'),
    path('aeroplan/', bbs.views.aeroplan_view, name='aerolan_view'),
]
