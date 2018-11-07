from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
	path('', UserViewSet.as_view({'get': 'list'}), name='index'),
	path('x/', list_file, name='list'),
]
