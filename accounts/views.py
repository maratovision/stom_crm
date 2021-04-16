from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status
from order.serializer import *
from schedule.serializer import DrTimeSerializer


class StomProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        doctor = StomProfile.objects.all()
        serializer = StomProfileSerializer(doctor, many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = StomProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data': 'Staff is created success'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SighUpView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = SighUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(views.APIView):

    def get(self, request, *args, **kwargs):
        client = UserProfile.objects.all()
        serializer = UserProfileSerializer(client, many=True)
        return Response(serializer.data)


class StomProfileDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        doctor = StomProfile.objects.get(id=kwargs['stomprofile_id'])
        serializer = StomProfileDetailSerializer(doctor)
        return Response(serializer.data)




class DrTimeDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        drtime = DrTime.objects.get(id=kwargs['drtime_id'],doctor_id=kwargs['stomprofile_id'])
        serializer = DrTimeSerializer(drtime)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
        drtime = DrTime.objects.get(id=kwargs['drtime_id'], doctor_id=kwargs['stomprofile_id'])
        doctor = drtime.doctor
        serializer = OrderHardSerializer(data=request.data)
        if serializer.is_valid():
            reason = serializer.data.get('reason')
            Order.objects.create(client=profile, doctor=doctor, dr_time=drtime, reason=reason)
            return Response({"Data": "ok!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

