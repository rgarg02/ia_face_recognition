# Generated by Django 2.2.2 on 2019-09-07 13:32

from django.db import migrations, models
import imageupload.models
import imageupload.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=imageupload.models.scramble_uploaded_filename, verbose_name='Uploaded Image')),
            ],
        ),
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=imageupload.models.scramble_uploaded_filename1, validators=[imageupload.validators.validate_file_extension], verbose_name='Uploaded Video')),
                ('name', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=10)),
                ('job', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
    ]