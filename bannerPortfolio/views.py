from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from django.http import  Http404 

from .models import *
from .ser import *


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

#################################################################################################
######################################### Hotel Views ###########################################
#################################################################################################

# get , list , delete view of hotel 
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    http_method_names = ['get', 'list','delete' ]


# Create View for hotel
class HotelCreateViewAPI(APIView):

    def post(self, request, id_banner):
        try:
            banner = Banner.objects.get(id=id_banner)
        except:
            raise Http404

        banner = Banner.objects.get(id=id_banner)
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save(banner=banner)
            return Response(serializer.data)
        return Response({'error':'please fill all fields'})



#################################################################################################
######################################### Category Views ###########################################
#################################################################################################

# get , list , delete view of hotel 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'list','delete']


# Create View for hotel
class CategoryCreateViewAPI(APIView):

    def post(self, request, id_banner):
        try:
            banner = Banner.objects.get(id=id_banner)
        except:
            raise Http404

        banner = Banner.objects.get(id=id_banner)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save(banner=banner)
            return Response(serializer.data)

        return Response({'error':'please fill all fields'})



#################################################################################################
########################### Complete Banner + (categories,hotels) ###############################
#################################################################################################

class BannerCompleteViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerCompleteSerializer




