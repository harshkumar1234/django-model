from django.contrib import admin
from .models import Members

@admin.register(Members)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display= ('id' , 'firstname' , 'lastname')
    
