from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class todoAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'date_added', 'achieved', )