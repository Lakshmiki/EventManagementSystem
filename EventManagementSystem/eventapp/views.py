from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from .forms import UserRegistrationForm, AdminRegistrationForm, UserProfileForm,VendorRegistrationForm,VendorLoginForm,HallForm_last,Booking_Form_last,EventForm
from .models import HallModel
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event,Venue_event
from django.urls import reverse
from .models import Event
from .forms import EmailForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vendor
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm,EquipmentForm
from .models import Venue, Booking,Equipment
from .forms import AvailabilityCheckForm, BookingForm,VenueSelectionForm,VenueForm,FoodPackageForm,RegistrationForm,CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings




# Create your views here.
@login_required(login_url='admin_login')


def register_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_register.html', {'form': form})
def login_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display_profile_user')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_login.html')

@login_required
def display_profile_view(request):
    return render(request, 'user_profile_display.html')

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('display_profile_user')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'update_user_profile.html', {'form': form})

@login_required
def delete_profile_view(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('user_register')
    return render(request, 'user_delete_profile.html')

def available_hall_view(request):
    available_halls=HallModel.objects.filter(is_available=True)
    context={
        'available_halls':available_halls
    }
    return render(request,'hall_available.html',context)

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('event_list')
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'
class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event_update.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'location']
    success_url = reverse_lazy('event_list')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')
class VenueCreateView(CreateView):
    model = Venue_event
    template_name = 'create_venue.html'
    fields = ['name', 'address', 'capacity']
    success_url = reverse_lazy('venue_list')
class VenueListView(ListView):
    model = Venue_event
    template_name = 'venue_list.html'
    context_object_name = 'venues'
class VenueDetailView(DetailView):
    model = Venue_event
    template_name = 'venue_detail.html'
    context_object_name = 'venue'
class VenueUpdateView(UpdateView):
    model = Venue_event
    template_name = 'venue_update.html'
    fields = ['name', 'address', 'capacity']
    success_url = reverse_lazy('venue_list')

class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('user_login')

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    success_url = reverse_lazy('user_profile')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user_login')

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user_profile_display.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user
def admin_register_view(request):
    if request.method=='POST':
        form=AdminRegistrationForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('password')
            if password!=cpassword:
                messages.error(request,"Passwords don't match")
            else:
                user=form.save(commit=False)
                user.set_password(password)
                user.save()
                messages.success(request,'registration successful.you can now log in')
                return redirect('admin_login')
    else:
        form=AdminRegistrationForm()
    return render(request,'admin_register_page.html',{'form':form})


def admin_login_view(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                messages.success(request, f'if you are now logged in as {username}.')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login_page.html', {'form': form})


def Admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('admin_dashboard')

    users = User.objects.all()
    vendors = Vendor.objects.all()
    events = Event.objects.all()

    context = {
        'users': users,
        'vendors': vendors,
        'events': events,
    }

    return render(request,'admin_dashboard.html',context)




def home_view(request):
    return render(request,'home.html')

@login_required
def delete_vendor(request, vendor_id):
    if not request.user.is_superuser:
        return redirect('home')

    vendor = Vendor.objects.get(id=vendor_id)
    vendor.delete()
    return redirect('admin_dashboard')
# def home_view(request):
#     return render(request,'home.html')
def UserRegisterview(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile_display')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')
@login_required
def view_user_profile(request):
    user=User.objects.get(user=request.user)
    return render(request, 'user_profile_display.html', {'user': user})

@login_required
def user_update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_view_profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'update_user_profile.html', {'form': form})

@login_required
def user_delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('user_view_profile')
    return render(request, 'user_delete_profile.html')
def home_user_view(request):
    return render(request,'home_user.html')
def upload_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('selected_venue_list')
    else:
        form = VenueForm()
    return render(request, 'upload_venue_list.html', {'form': form})



def book_half_view(request, venue_id,date,half):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.venue_id = venue_id
            booking.date = date
            booking.half = half
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form,'venue': venue})
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

class EventListView_user(ListView):
    model = Event
    template_name = 'event_list_user.html'
    context_object_name = 'events'
class EventDetailView_user(DetailView):
    model = Event
    template_name = 'event_detail_user.html'
    context_object_name = 'event'
def upload_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')  # Replace with your equipment list URL name
    else:
        form = EquipmentForm()
    return render(request, 'upload_equipment.html', {'form': form})
def equipment_list_view(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})

def upload_food_package_view(request):
    if request.method == 'POST':
        form = FoodPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_package_list')
    else:
        form = FoodPackageForm()
    return render(request, 'upload_food_package.html', {'form': form})
def food_package_list_view(request):
    packages = FoodPackage.objects.all()
    return render(request, 'food_package_list.html', {'packages': packages})
def user_for_admin_view(request):

    users = User.objects.all()

    context = {
        'users': users
    }


    return render(request,'user_for_admin.html',context)


def vendor_registration_view(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_login')  # Redirect to vendor login page after registration
    else:
        form = VendorRegistrationForm()

    return render(request, 'vendor_registration.html', {'form': form})


def vendor_login_view(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                vendor = Vendor_model.objects.get(username=username)
                if vendor.password == password:
                    # Authentication successful, create session
                    request.session['vendor_id'] = vendor.id
                    return redirect('vendor_dashboard')  # Replace with your vendor dashboard URL name
                else:
                    form.add_error(None, 'Invalid username or password.')
            except Vendor.DoesNotExist:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = VendorLoginForm()

    return render(request, 'vendor_login.html', {'form': form})
def vendor_dashboard_view(request):
    vendor_id = request.session.get('vendor_id')
    if vendor_id:
        vendor = Vendor_model.objects.get(id=vendor_id)
        return render(request, 'vendor_dashboard.html', {'vendor': vendor})
    else:
        return redirect('vendor_login')
def vendor_logout_view(request):
    logout(request)
    return redirect('vendor_login')
def vendor_for_admin_view(request):
    vendors = Vendor_model.objects.all()
    context = {
        'vendors': vendors
    }


    return render(request,'vendor_for_admin.html',context)
def update_vendor(request, vendor_id):
    if not request.user.is_superuser:
        return redirect('home')

    vendor = Vendor_model.objects.get(id=vendor_id)

    if request.method == 'POST':
        vendor.username = request.POST['username']
        vendor.email = request.POST['email']
        vendor.company_name = request.POST['company_name']
        vendor.contact_person = request.POST['contact_person']
        vendor.save()
        return redirect('admin_dashboard')

    context = {'vendor': vendor}
    return render(request, 'update_vendor.html', context)
def user_and_vendor_dashboard_view(request):
    return render(request,'user_and_vendor_dashboard.html')

def user_delete_for_admin_view(request,user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_for_admin')  # Redirect to appropriate page after deletion

    return render(request, 'user_delete_for_admin.html', {'user': user})

def vendor_delete_profile_admin_view(request,vendor_id):
    vendor = get_object_or_404(Vendor_model,id=vendor_id)

    if request.method == 'POST':
        vendor.delete()
        messages.success(request, 'Vendor profile deleted successfully.')
        return redirect('vendor_for_admin')

    return render(request, 'vendor_delete_profile_admin.html', {'vendor': vendor})
def create_hall_last_view(request):
    if request.method == 'POST':
        form = HallForm_last(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hall_list_last')
    else:
        form = HallForm_last()
    return render(request, 'create_hall_last.html', {'form': form})
def hall_list_last_view(request):
    halls = Hall_last_Model.objects.all()
    return render(request, 'hall_list_last.html', {'halls': halls})
def book_hall_last_view(request):
    if request.method == 'POST':
        form = Booking_Form_last(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('booking_confirmation')
                # redirect('booking_list'))  # Redirect to the booking list or another appropriate page
    else:
        form = Booking_Form_last()
    return render(request, 'book_hall_last.html', {'form': form})
def book_list_last_view(request):
    data=Booking_last_model.objects.all()
    return render(request,'booked_list.html',{'data':data})
def booking_confirmation_view(request):
    return render(request,'booking_confirmation.html')
def UserRegisterview(request):
    form=UserRegistrationForm()
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            subject = 'event management'
            message = 'Thank you for registering in ever after event'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            user = form.save()
            login(request, user)
        return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_register.html', {'form': form})

def change_password_user_view(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            if new_password == confirm_new_password:
                user.password = make_password(new_password)
                user.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect('password_change_done_user')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'change_password_user.html')

def password_change_done_user_view(request):
    return render(request, 'password_change_done_user.html')
def user_logout_view(request):
    logout(request)
    return redirect('logout_done_user')
def logout_done_user_view(request):
    return render(request, 'logout_done_user.html')
def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')
def admin_about_view(request):
    return render(request,'admin_about_page.html')
def user_about_page_view(request):
    return render(request,'user_about_page.html')
def vendor_logout_view(request):
    logout(request)
    return redirect('vendor_login')
def upload_equipment_vendor(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'upload_equipment_vendor.html', {'form': form})
def upload_food_package_vendor_view(request):
    if request.method == 'POST':
        form = FoodPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_package_list')
    else:
        form = FoodPackageForm()
    return render(request, 'upload_food_package_vendor.html', {'form': form})
def vendor_about_page_view(request):
    return render(request,'vendor_about_page.html')
