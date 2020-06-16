from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from .models import UploadImage, UploadVideo
from imageupload_rest.serializers import UploadImageSerializer,UploadVideoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
import cv2
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
@api_view(('GET','POST'))

def home(request):
    if request.method == 'GET':
        snippets = UploadImage.objects.all()
        serializer = UploadImageSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UploadImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            path = serializer.data['image'].split('/')[-1]
            finalpath = os.path.join(BASE_DIR,'uploaded_media',path)
            from .face import facerec
            print(finalpath)
            res = facerec(finalpath)
            d = serializer.data
            if res!="false":
                d['response'] = res
                return Response(d, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(('GET','POST'))
def video(request):
    if request.method == 'GET':
        snippets = UploadVideo.objects.all()
        serializer = UploadVideoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UploadVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            path = serializer.data['video'].split('/')[-1]
            print(path)
            finalpath = os.path.join(BASE_DIR,'uploaded_media','videos',path)
            record = serializer.data
            from .train import add
            res = add(finalpath,record['uID'])
            d = serializer.data
            d['response'] = res
            if res=="User Added":
                from .train import getImagesID
                getImagesID
            return Response(d, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


