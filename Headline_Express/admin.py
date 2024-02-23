from django.contrib import admin
from .models import subs_info , department_cat , departments , news

# Register your models here.

admin.site.register(subs_info)
admin.site.register(department_cat)
admin.site.register(departments)
admin.site.register(news)

