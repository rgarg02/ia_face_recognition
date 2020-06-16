from rest_framework import serializers
from imageupload.models import UploadImage, UploadVideo

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image', )

class UploadVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadVideo
        fields = ('pk', 'video' , 'name', 'age', 'job', 'phone','uID' )


