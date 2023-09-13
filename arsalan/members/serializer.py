from rest_framework import serializers

from arsalan.members.views import ReactView
from . models import *

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReactView
		fields = ['name', 'email']
