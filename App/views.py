import re
from cv2 import IMWRITE_JPEG_CHROMA_QUALITY
from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from io import BytesIO
import urllib.request
from PIL import Image
import requests
from io import BytesIO
import cv2
import face_recognition
from skimage import io
import json
from json import JSONEncoder
from rest_framework import status
from .models import User
import pymongo

client = pymongo.MongoClient('mongodb+srv://root:hackonroot@cluster0.nz2mi.mongodb.net/hackon?retryWrites=true&w=majority')
#Define Db Name
db = client['hackon']

#Define Collection
user_collection = db['users']
@api_view(['GET'])

def home(request):
    try:

        html = "<h1>Html</h1>"
        return HttpResponse(html)
    except:
        raise APIException("There was a problem!")

# urllib.request.urlretrieve("https://i.imgur.com/ExdKOOz.png", "sample.png")
@api_view(['POST'])
def compare_faces(request):
    try:
        if request.method == "POST":
                img_one_url = request.data['img_one_url']
                img_two_url = request.data['img_two_url']
                
                img1 = io.imread(img_one_url)
                rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
                img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

                img2 = io.imread(img_two_url)
                rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

                result = face_recognition.compare_faces([img_encoding1], img_encoding2)

                resultDict = {
                        "result": str(result),
                }
        else:
                resultDict = {"result": "use post method"}
        return JsonResponse(json.dumps(resultDict), safe=False, status=status.HTTP_308_PERMANENT_REDIRECT)

    except:
        raise APIException("There was a problem!")

@api_view(['POST'])
def add_user(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            email = request.data['email']
            results1 = User.objects.filter(username__text_search=username)
            results2 = User.objects.filter(email__text_search=email)
            print(results1)

            # user = User()
            # user.username = request.data['username']
            # user.full_name = request.data['full_name']   
            # user.password = request.data['password']
            # user.img_url = request.data['img_url']
            # user.email = request.data['email']
            # img = io.imread(request.data['img_url'])
            # rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # img_encoding = face_recognition.face_encodings(rgb_img)[0]
            # user.encoding = str(img_encoding.tolist())
            # user.save()
            return HttpResponse("userCreated")
        else:
            return HttpResponse("Invalid request")    
    except:
        raise APIException("Error creating user")

