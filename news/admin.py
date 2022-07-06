from django.contrib import admin

from news.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", 'data', 'is_active')

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)



# Register your models here.
