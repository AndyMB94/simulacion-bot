from django.urls import path
from .views import receive_data, get_data

urlpatterns = [
    path('receive/', receive_data, name='receive_data'),
    path('get-data/', get_data, name='get_data'),
]