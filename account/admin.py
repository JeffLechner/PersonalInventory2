from django.contrib import admin

from .models import Account, Area, Container, InventoryItem, Place, Profile


class AccountList(admin.ModelAdmin):
	list_display = ('accountName', )
	list_filter = ('accountName', )
	search_fields = ('accountName', )
	ordering = ['accountName']


class ProfileList(admin.ModelAdmin):
	list_display = ('name', 'user')
	list_filter = ('name', 'user')
	search_fields = ('name', 'user')
	ordering = ['user', 'name']


class InventoryItemList(admin.ModelAdmin):
	list_display = ('name', 'value', 'category', 'profile')
	list_filter = ('name', 'profile', 'category')
	search_fields = ('name', 'account', 'category', 'profile')
	ordering = ['profile', 'name', 'category', 'value']


class PlaceList(admin.ModelAdmin):
	list_display = ('name', 'id', 'profile')
	list_filter = ('name', 'id', 'profile')
	search_fields = ('id', 'name', 'profile')
	ordering = ['name', 'id', 'profile']


class AreaList(admin.ModelAdmin):
	list_display = ('name', 'place', 'id',  'profile' )
	list_filter = ('id', 'name', 'place', 'profile')
	search_fields = ('id', 'name', 'place', 'profile')
	ordering = ['place', 'name', 'profile', 'id', ]


class ContainerList(admin.ModelAdmin):
	list_display = ('name', 'area', 'id',  'profile' )
	list_filter = ('id', 'name', 'area', 'profile')
	search_fields = ('id', 'name', 'area', 'profile')
	ordering = ['area', 'name', 'profile', 'id', ]


admin.site.register(Account, AccountList)
admin.site.register(Profile, ProfileList)
admin.site.register(InventoryItem, InventoryItemList)
admin.site.register(Place, PlaceList)
admin.site.register(Area, AreaList)
admin.site.register(Container, ContainerList)