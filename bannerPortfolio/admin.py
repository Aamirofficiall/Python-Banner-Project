from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget

from django.contrib import admin
from django import forms

from .models import *


admin.site.unregister(Group)



class ConferenceAdminForm(forms.ModelForm):
    
    class Meta:
        model = Conference
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control '
        self.fields['detail_title'].widget.attrs['class'] = 'form-control'   
        self.fields['conference_date'].widget.attrs['class'] = 'form-control vDateField'   
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['venue'].widget.attrs['class'] = 'form-control'
        # self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['registration'].widget.attrs['class'] = 'form-control'


class HotelAdminForm(forms.ModelForm):
    
    class Meta:
        model = Hotel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control mr-3  '
        self.fields['redirect_url'].widget.attrs['class'] = 'form-control mr-3'   

class HotelInline(admin.TabularInline):
    model = Hotel
    form = HotelAdminForm

class ConferenceAdmin(admin.ModelAdmin):
    form = ConferenceAdminForm
    list_display = ("id", "title","detail_title","conference_date","address","venue","is_featured","city","country",)

    inlines = [
        HotelInline,
    ]


admin.site.register(Conference, ConferenceAdmin)


