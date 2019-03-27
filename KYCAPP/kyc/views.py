from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import requests
from django.http import JsonResponse
from rest_framework.response import Response

# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


from django.shortcuts import render

# Create your views here.
'''
class kycList(APIView):
    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))


    def get(self,request):
       e=Customer.objects.all()
       serializer=CustomerSerializer(e,many=True)
       return Response(serializer.data)



        #id=request.GET.get('id')
        #extract=Customer.filter(id)
        #serializer = CustomerSerializer(extract,many=True)
        #return JsonResponse(serializer.data,safe=False)

'''