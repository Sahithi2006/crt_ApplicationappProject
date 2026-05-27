from django.urls import path
from .views import add_employee,get_employee_details
#http://127.0.0.1:8000/first/wishes
urlpatterns=[
    path("wishes",greet),
    path("details",get_details)
]