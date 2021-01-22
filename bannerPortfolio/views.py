from django.contrib.auth import logout as auth_logout

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render,redirect
from django.shortcuts import render
from rest_framework import viewsets
from django.http import  Http404 

from .models import *
from .ser import *



class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer



def logout(request):
    auth_logout(request)
    return render(request,'logout.html')