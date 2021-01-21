from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *


admin.site.unregister(Group)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Category)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("id", "category_title","register_price","register_late_price")


class HotelInline(admin.TabularInline):
    model = Hotel

class CategoryInline(admin.TabularInline):
    model = Category

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "banner_title","banner_dateOfEvent","tab1_title","tab2_title","tab3_title")

    inlines = [
        HotelInline,
        CategoryInline,
    ]


