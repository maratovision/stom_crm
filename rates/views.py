from rest_framework import views, status
from rest_framework.response import Response
from .serializer import *


class RateView(views.APIView):

    def get(self, request, *args, **kwargs):
        rate = Rate.objects.all()
        serializer = RateSerializer(rate, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Thanks for rate'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
