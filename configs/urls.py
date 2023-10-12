from django.urls import path
# from cars.views import TestOneView, TestTwoView
from cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    # path('one', TestOneView.as_view()),
    # path('two/<int:pk>', TestTwoView.as_view())
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]