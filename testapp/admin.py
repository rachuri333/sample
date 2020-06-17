from django.contrib import admin
from .models import persondetail
# Register your models here.
class detailadmin(admin.ModelAdmin):
    list_display=['Name','Phone']

admin.site.register(persondetail,detailadmin)
