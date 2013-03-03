# Create your views here.

from rest_framework import generics
from models import Picture
from serializers import PictureSerializer


class PictureList(generics.ListCreateAPIView):
    model = Picture
    serializer_class = PictureSerializer


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Picture
    serializer_class = PictureSerializer
