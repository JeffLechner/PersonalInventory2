from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
	path('', views.home_view, name='home'),

	path('signup', views.signup_view, name='sign-up'),
	path('dashboard', views.dashboard_view, name='dashboard'),
	path('selectProfile', views.selectProfile, name='selectProfile'),
	path('addProfile', views.addProfile, name='addProfile'),

	path('addItem/<str:pk>', views.addItem, name='addItem'),
	path('container/<str:c_id>/editItem/<str:i_id>', views.editItem, name='editItem'),
	path('lendItem/<str:pk>', views.lendItem, name='lendItem'),
	path('returnItem/<str:pk>', views.returnItem, name='returnItem'),
	path('deleteItem/<str:pk>', views.deleteItem, name='deleteItem'),

	path('addPlace', views.addPlace, name='addPlace'),
	path('editPlace/<str:pk>', views.editPlace, name='editPlace'),
	path('viewPlace/<str:pk>', views.viewPlace, name='viewPlace'),
	path('deletePlace/<str:pk>', views.deletePlace, name='deletePlace'),

	path('addArea/<str:pk>', views.addArea, name='addArea'),
	path('editArea/<str:pk>', views.editArea, name='editArea'),
	path('viewArea/<str:pk>', views.viewArea, name='viewArea'),
	path('deleteArea/<str:pk>', views.deleteArea, name='deleteArea'),

	path('addContainer/<str:pk>', views.addContainer, name='addContainer'),
	path('editContainer/<str:pk>', views.editContainer, name='editCont'),
	path('viewContainer/<str:pk>', views.viewContainer, name='viewContainer'),
	path('deleteContainer/<str:pk>', views.deleteContainer, name='deleteContainer'),

	path('searchItems', views.searchItems, name='searchItems'),
	path('addCategory/<str:pk>', views.addCategory, name='addCategory')
]
