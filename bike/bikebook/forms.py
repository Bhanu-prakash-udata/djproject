from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from bikebook.models import Address,Addbike


class Userreg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email']
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your first name",
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your last name",
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your full name",
			}),
		"email":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your mailid",
			}),
		}


class Ad(ModelForm):
	class Meta:
		model = Address
		fields = ["firstname","lastname","username","emailid","address","pincode","age"]
		widgets = {
		"firstname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter your first name",
			}),
		"lastname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter your last name",
			}),
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter your  name",
			}),
		"emailid":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter a valid email address",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"enter your address",
			}),
		"pincode":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"enter your area pincode"
			}),
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"enter your age",
			})

		}

class Add(forms.ModelForm):
	class Meta:
		model = Addbike
		fields = ["brandname","brandlogo","bikemodel","bikefrontimage","bikebackimage","bikeleftimage","bikerightimage","bikecost","bikecc","fuelinjectiontype","location"]
		widgets ={
			"brandname":forms.Select(attrs={
				"class":"form-control custom-select branch",
				"placeholder":"enter the name of company",
				}),
			"email":forms.TextInput(attrs={
				"class":"form-control",
				"placeholder":"enter the name of bike",
				}),
			"bikecost":forms.NumberInput(attrs={
				"class":"form-control",
				"placeholder":"enter the bike cost",
				}),
			"bikecc":forms.NumberInput(attrs={
				"class":"form-control",
				"placeholder":"enter the cc bike",
				}),
			"location":forms.TextInput(attrs={
				"class":"form-control",
				"placeholder":"enter the showroom location",
				}),
			}

			# branch = forms.CharField(widget=forms.Select(choices=br,attrs={'class':"form-control custom-select branch"}))