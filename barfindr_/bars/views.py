from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bars.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BarViewSet(viewsets.ModelViewSet):
	"""
	Bar endpoint
	"""
	queryset = Bar.objects.all()
	serializer_class = BarSerializer