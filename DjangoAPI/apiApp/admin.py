from django.contrib import admin
from apiApp.models import Test
# Register your models here.



@admin.register(Test)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')  # 在后台列表下显示的字段