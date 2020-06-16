from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from imageupload_rest.viewsets import UploadImageViewSet, UploadVideoViewSet
from imageupload.views import home, video



app_name = 'reviews'
urlpatterns = [

    path('images/',home,name='home'),
    path('videos/',video,name='video'),
]

