from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions import IsAdminWriteOrIsAuthenticatedRead

from .filter import CarFilter
from .models import CarModel
from .serializer import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)


class AddPhotoByCarIdView(UpdateAPIView):
    permission_classes = (IsAdminWriteOrIsAuthenticatedRead,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)
