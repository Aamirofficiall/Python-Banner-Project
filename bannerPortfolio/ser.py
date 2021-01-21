from rest_framework import serializers
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_title','register_price','register_late_price']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','title','image']


class BannerCompleteSerializer(serializers.ModelSerializer):
    Hotelbanner = HotelSerializer(many=True)
    Categorybanner = CategorySerializer(many=True)


    def create(self, validated_data):
        hotels_data = validated_data.pop('Hotelbanner')
        catagories_data = validated_data.pop('Categorybanner')
        banner = Banner.objects.create(**validated_data)

        for hotel_data in hotels_data:
            Hotels.objects.create(banner=banner, **hotel_data)
        for catagory_data in catagories_data:
            Hotels.objects.create(banner=banner, **catagory_data)            
        return banner 




    class Meta:
        model = Banner
        fields = [
            'banner_title','banner_dateOfEvent','banner_address',
            'banner_image','tab1_title','tab1_description','tab2_title',
            'tab2_description','tab3_title','tab3_description','tab3_venue','tab3_address',
            'Hotelbanner','Categorybanner'
            ]


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'
  


