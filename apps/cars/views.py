from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filter import car_filtered_queryset
from .models import CarModel
from .serializer import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

