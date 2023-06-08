from django.contrib import admin
from .models import myTodo

# Register your models here.
@admin.register(myTodo)
class myTodoAdmin(admin.ModelAdmin):
    list_display = ('task',)
    
