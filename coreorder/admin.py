from django.contrib import admin
from .models import InitialCalOrder
# Register your models here.

@admin.register(InitialCalOrder)
class InitialOrderAdmin(admin.ModelAdmin):
    list_display = ['subject', 'accademic_level', "price", 'pages']
    
    
