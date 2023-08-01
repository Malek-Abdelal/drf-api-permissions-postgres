from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .serializer import CarSerializer
from .permissions import IsOwnerOrReadOlny
# Create your views here.

class CarListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOlny]