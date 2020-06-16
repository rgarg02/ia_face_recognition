from rest_framework import viewsets
from imageupload_rest.serializers import UploadImageSerializer, UploadVideoSerializer
from imageupload.models import UploadImage, UploadVideo
from .imagefunction import image
from rest_framework import status

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
    
class UploadVideoViewSet(viewsets.ModelViewSet):
    queryset = UploadVideo.objects.all()
    serializer_class = UploadVideoSerializer
    

