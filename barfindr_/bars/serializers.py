from django.contrib.auth.models import User, Group
from bars.models import Bar
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class BarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bar
		fields = ('name', 'address', 'locx', 'locy', 'hours_open', 'hours_close')