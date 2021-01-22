from rest_framework import serializers
from .models import *





  

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','title','image','redirect_url']

class ConferenceSerializer(serializers.ModelSerializer):
    conferenceHotel = HotelSerializer(many=True)


    def create(self, validated_data):
        hotels_data = validated_data.pop('conferenceHotel')
        conference = Conference.objects.create(**validated_data)
        for hotel_data in hotels_data:
            Hotel.objects.create(conference=conference, **hotel_data)
    
        return conference 
    class Meta:
        model = Conference
        fields = '__all__'
