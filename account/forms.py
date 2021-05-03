from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Area, Container, InventoryItem, Place, Profile, Category


class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		label='',
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		)
	)

	username = forms.CharField(
		label='',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Confirm Password",
				"class": "form-control"
			}
		)
	)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class InventoryItemForm(forms.ModelForm):
	name = forms.CharField(max_length=70, required=True, help_text='', label='Name')
	image= forms.ImageField(required=True, label="image")
	value=forms.IntegerField(required=True, label="Initial Value")
	extraDetails = forms.CharField(max_length=300, required=False, label='Details')
	increasing_ratio_in_percentage= forms.IntegerField(required=True, label="Increase by Percent")
	interval_of_days = forms.IntegerField(required=True, label="Interval of days")
	current_value = forms.IntegerField(required=True, label="Current Value", help_text="Increase Item Value overtime")
	class Meta:
		model = InventoryItem
		fields = ('name',  'category', 'image', 'extraDetails', 'value', 'current_value', 'increasing_ratio_in_percentage', 'interval_of_days')


class ContainerForm(forms.ModelForm):
	class Meta:
		model = Container
		fields = ('name', 'image')


class PlaceForm(forms.ModelForm):

	class Meta:
		model = Place
		fields = ('name', 'image')


class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = ('name', 'image')


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)


class SelectProfileForm(forms.Form):
	id = forms.UUIDField()


SEARCH_CHOICES= [
    ('place', 'Place'),
    ('area', 'Area'),
    ('container', 'Container'),
    ('item', 'Items'),
    ]


class SearchItemsForm(forms.Form):
	query = forms.CharField(max_length=100)
	favorite_fruit = forms.CharField(label='Select Search type?', widget=forms.Select(choices=SEARCH_CHOICES))


class LendForm(forms.Form):
	toFriend = forms.BooleanField(required=False)
	name = forms.CharField(max_length=100)


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name',)
	name = forms.CharField(max_length=100)
