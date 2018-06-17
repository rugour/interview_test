from django.contrib import admin

from .models import APIUser

class APIUserAdmin(admin.ModelAdmin):
	"""docstring for APIUserAdmin"""
	model = APIUser
	list_display = ('login', 'avatar')
	search_fields = ['added_on', 'email', 'login']

admin.site.register(APIUser, APIUserAdmin)