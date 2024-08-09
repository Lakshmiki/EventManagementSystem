from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from .models import Venue, Booking, Equipment, FoodPackage, Venue_event, Vendor_model, Hall_last_Model, Booking_last_model,Event


class Admin_login_form(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'placeholder':'Username'
    }))
    password=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form_control',
        'type':'password',
        'placeholder':'Password'
    }))


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class AdminLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    # for hidden passwords
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'cpassword']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(UserChangeForm):
    password = None  # Exclude password field

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'capacity', 'location', 'image']

class VenueSelectionForm(forms.Form):
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(), empty_label="Select Venue")

class AvailabilityCheckForm(forms.Form):
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(), empty_label="Select Venue")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['venue', 'date', 'half']
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'quantity']
class FoodPackageForm(forms.ModelForm):
    class Meta:
        model = FoodPackage
        fields = ['name', 'description', 'price', 'quantity_available']
class VendorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Vendor_model
        fields = ['username', 'password', 'company_name', 'contact_person', 'email']
class VendorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class HallForm_last(forms.ModelForm):
    class Meta:
        model = Hall_last_Model
        fields = ['name', 'location', 'capacity', 'description']
class Booking_Form_last(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Booking_last_model
        fields = ['hall', 'date', 'start_time', 'end_time']
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'image']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }