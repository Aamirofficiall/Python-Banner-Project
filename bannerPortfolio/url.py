from rest_framework.routers import DefaultRouter
from django.urls import path, include,re_path
from .views import ConferenceViewSet

router = DefaultRouter()
router.register('conference', ConferenceViewSet, basename='conference')


urlpatterns = [
       path('',include(router.urls)),
       
]
