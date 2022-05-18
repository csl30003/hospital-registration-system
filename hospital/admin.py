from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Patient,Doctor,TimeNumber,Department,Register])

admin.site.site_header = '后台管理系统'
admin.site.index_title = '首页'