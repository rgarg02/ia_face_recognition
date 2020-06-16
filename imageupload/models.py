from django.db import models
import uuid
from .validators import validate_file_extension
def scramble_uploaded_filename(instance,filename):
    extension = filename.split(".")[-1]

    reformated = "{}.{}".format(uuid.uuid4(),extension)

    return reformated
    
def scramble_uploaded_filename1(instance,filename):
    extension = filename.split(".")[-1]
    reformated = "videos/"+"{}.{}".format(uuid.uuid4(),extension)

    return reformated

class UploadVideo(models.Model):
    video = models.FileField('Uploaded Video',upload_to=scramble_uploaded_filename1, validators=[validate_file_extension] )
    name = models.CharField(max_length=50,default='')
    age = models.CharField(max_length=10,default='')
    job = models.CharField(max_length=30,default='')
    phone = models.CharField(max_length=10,default='')
    uID = models.CharField(max_length=10,default='')
class UploadImage(models.Model):
    image = models.ImageField('Uploaded Image', upload_to=scramble_uploaded_filename)

