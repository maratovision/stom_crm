from rest_framework import views
from rest_framework.response import Response

from .serializer import *
from .models import *


class DrTimeView(views.APIView):

    def get(self, request, *args, **kwargs):
        times = DrTime.objects.all()
        serializer = DrTimeSerializer(times, many=True)
        return Response(serializer.data)
