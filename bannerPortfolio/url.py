from rest_framework.routers import DefaultRouter
from django.urls import path, include
# from .views import BannerViewSet, HotelViewSet
from .views import BannerCompleteViewSet,BannerViewSet,HotelViewSet,HotelCreateViewAPI,CategoryViewSet,CategoryCreateViewAPI

router = DefaultRouter()
router.register('banner', BannerViewSet, basename='banner')
router.register('category', CategoryViewSet, basename='category')
router.register('hotel', HotelViewSet, basename='hotel')
router.register('bannerComplete', BannerCompleteViewSet, basename='bannerComplete')



urlpatterns = [

       path('',include(router.urls)),
       path('<int:id_banner>/hotel/',HotelCreateViewAPI.as_view() , name='hotelCreateView'), 
       path('<int:id_banner>/category/',CategoryCreateViewAPI.as_view() , name='categoryCrateView'), 
       

]
