from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status


class StomProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        doctor = StomProfile.objects.all()
        serializer = StomProfileSerializer(doctor, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StomProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Staff is created success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

