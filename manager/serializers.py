
import json
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'user_name', 'password')
