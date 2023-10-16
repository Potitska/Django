from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filter import CarFilter
from .models import CarModel
from .serializer import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
