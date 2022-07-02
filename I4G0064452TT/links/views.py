from django.shortcuts import render
from .models import Link
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,GenericAPIView,RetrieveAPIView
#from multiprocessing import AuthenticationError
from .serializers import LinkSerializer

# Create your views here.


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetaiApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer








    


