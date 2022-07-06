from django.contrib import admin

from feedback.models import *


class PeoplesAdmin(admin.ModelAdmin):
    list_display = ("Телефон", "Имя", "Тема", 'created', 'id')

    class Meta:
        model = Peoples


admin.site.register(Peoples, PeoplesAdmin)


