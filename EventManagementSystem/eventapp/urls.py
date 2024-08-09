from django.contrib.auth import admin
from django.urls import path

from . import views
from .views import *
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    VenueListView,
    VenueCreateView,
    EventListView_user,
    EventDetailView_user

)
from .views import Admin_dashboard_view, update_profile_view, delete_profile_view, update_vendor, delete_vendor
from .views import  book_half_view,user_for_admin_view

urlpatterns=[

    path('admin_register/',admin_register_view,name='admin_register'),
    path('admin_login/',admin_login_view,name='admin_login'),
    path('admin_dashboard/',Admin_dashboard_view,name='admin_dashboard'),
    path('user_register/',UserRegisterview,name='user_register'),
    path('user_login/',login_user_view,name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('display_profile_user/',display_profile_view,name='display_profile_user'),
    path('create_event/',EventCreateView.as_view(), name='create_event'),
    path('event_list/',EventListView.as_view(),name='event_list'),
    path('event_detail/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event_update/<int:pk>/', EventUpdateView.as_view(), name='event_update'),
    path('event_delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('event_venue_create/',VenueCreateView.as_view(),name='create_venue'),
    path('event_venue_list/',VenueListView.as_view(),name='venue_list'),
    path('event_venue_detail/<int:pk>/',VenueDetailView.as_view(), name='venue_detail'),
    path('event_venue_update/<int:pk>/',VenueUpdateView.as_view(),name='venue_update'),
    path('update_user/', user_update_profile, name='update_user'),
    path('delete_user/', user_delete_profile, name='delete_user'),
    path('update_vendor/<int:vendor_id>/', update_vendor, name='update_vendor'),
    path('delete_vendor/<int:vendor_id>/', delete_vendor, name='delete_vendor'),
    path('home/',home_view,name='home'),
    path('home_user/',home_user_view,name='home_user'),
    path('user_profile_update/',update_profile_view, name='user_update_profile'),
    path('user_profile_delete/',delete_profile_view, name='user_profile_delete'),
    path('upload_venue_list/', upload_venue, name='upload_venue_list'),
    path('book_half/<int:venue_id>/', book_half_view, name='book_half'),
    path('booking_confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('event_list_user/',EventListView_user.as_view(),name='event_list_user'),
    path('event_detail_user/<int:pk>/',EventDetailView_user.as_view(),name='event_detail_user'),
    path('upload_equipment_admin/', views.upload_equipment, name='upload-equipment_admin'),
    path('equipment_list/', views.equipment_list_view, name='equipment_list'),
    path('upload_food_package/', views.upload_food_package_view, name='upload_food_package'),
    path('food_package_list/',views.food_package_list_view,name='food_package_list'),
    path('user_for_admin/',user_for_admin_view,name='user_for_admin'),
    path('vendor_reg/',vendor_registration_view,name='vendor_reg'),
    path('vendor_login/',vendor_login_view,name='vendor_login'),
    path('vendor_dashboard/',vendor_dashboard_view,name='vendor_dashboard'),
    path('vendor_logout/',vendor_logout_view, name='vendor_logout'),
    path('vendor_for_admin/',vendor_for_admin_view,name='vendor_for_admin'),
    path('user_and_vendor_dashboard/',user_and_vendor_dashboard_view,name='user_and_vendor_dashboard'),
    path('user_delete_for_admin/<int:user_id>/',user_delete_for_admin_view,name='user_delete_for_admin'),
    path('vendor_delete_profile_admin/<int:vendor_id>/',vendor_delete_profile_admin_view,name='vendor_delete_profile_admin'),
    path('create_hall_last/', create_hall_last_view, name='create_hall_last'),
    path('hall_list_last/', hall_list_last_view, name='hall_list_last'),
    path('book_hall_last/', book_hall_last_view, name='book_hall_last'),
    path('booked_list/',book_list_last_view,name='booked_list'),
    path('booking_confirmation/',booking_confirmation_view,name='booking_confirmation'),
    path('change_password_user/', change_password_user_view, name='change_password_user'),
    path('password_change_done_user/',password_change_done_user_view, name='password_change_done_user'),
    path('logout_user/', user_logout_view, name='logout_user'),
    path('logout_done_user/', logout_done_user_view, name='logout_done_user'),
    path('admin_logout/',admin_logout_view,name='admin_logout'),
    path('admin_about_page/',admin_about_view,name='admin_about_page'),
    path('user_about_page/',user_about_page_view,name='user_about_page'),
    path('vendor_logout/',vendor_logout_view,name='vendor_logout'),
    path('vendor_upload_equipment/',upload_equipment_vendor,name='vendor_upload_equipment'),
    path('vendor_upload_food/',upload_food_package_vendor_view,name='vendor_upload_food'),
    path('vendor_about_page/',vendor_about_page_view,name='vendor_about_page')
]