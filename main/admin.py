from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import date2jalali, datetime2jalali

from . import models


class ItemAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'cat' , 'is_offer' ]
    fields = (
        'created', 'title', 'slug', 'image', ('cat', 'is_offer'),'views', 'body'
    )
    search_fields = ['title', 'slug', 'cat__name']
    list_filter = ['cat', 'is_offer', ]
    

    ordering = ('-created', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'get_item_count']
    search_fields = ['name', 'slug']


class UserMessageAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'get_created']
    search_fields = ['name', 'subject', 'message']
    
    def get_created(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    
    get_created.short_description = 'تاریخ ایجاد'
    get_created.admin_order_field = 'created'


class GalleryImageAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'get_created']
    search_fields = ['name', ]
    
    def get_created(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
    
    get_created.short_description = 'تاریخ ایجاد'
    get_created.admin_order_field = 'created'


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.UserMessage, UserMessageAdmin)
admin.site.register(models.GalleryImage, GalleryImageAdmin)
admin.site.register(models.Company)

admin.site.unregister(Group)
