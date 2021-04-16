from rest_framework.response import Response
from .serializer import *
from rest_framework import views, status
from .models import *


class OrderView(views.APIView):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)






