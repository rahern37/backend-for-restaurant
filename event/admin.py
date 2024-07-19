from django.contrib import admin


from .models import Event

# create a class for the admin-model integration
class EventAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("title","description","date")

admin.site.register(Event,EventAdmin)
