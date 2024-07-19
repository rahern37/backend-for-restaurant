# import serializers from the REST framework
from rest_framework import serializers

from .models import Event

# create a serializer class
class EventSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Event
		fields = ('title','description','date')
