from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about,name="my_about"),
    path('blog',views.blog,name='my_blog'),
    path('contact',views.contact,name='my_contact'),
    path('services',views.services,name='my_services'),


]