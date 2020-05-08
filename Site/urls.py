from django.urls import path
from . import views
from .views import index,about,contact,progect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('send/',views.contactform, name='send'),
    path('', index, name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('progect/',progect,name='progect'),
]