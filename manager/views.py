from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import UserSerializer, User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


def list_file(request):
	import os, json
	tmp = os.listdir("./")
	d_tmp = {}
	for i in range(1, len(tmp)):
		if os.path.isfile(tmp[i]):
			t = "file"
		elif os.path.isdir(tmp[i]):
			t = "dir"
		d_tmp[str(i) + " " + t] = tmp[i]
	x = json.dumps(d_tmp)
	return HttpResponse(x)
