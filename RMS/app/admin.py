from django.contrib import admin
from .models import Register,Station,Train,Detail,Contact
# Register your models here.
admin.site.register(Detail)
admin.site.register(Contact)
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
	list_display=('id','name','email')

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
	list_display=('id','station')

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
	list_display=('id','name','no')
