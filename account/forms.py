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

	class Meta:
		model = InventoryItem
		fields = ('name', 'image', 'value', 'extraDetails', 'increasing_ratio_in_percentage', 'interval_of_days')


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


class SearchItemsForm(forms.Form):
	query = forms.CharField(max_length=100)


class LendForm(forms.Form):
	toFriend = forms.BooleanField(required=False)
	name = forms.CharField(max_length=100)


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name',)
	name = forms.CharField(max_length=100)
