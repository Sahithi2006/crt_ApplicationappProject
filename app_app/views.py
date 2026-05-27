from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from http import HTTPStatus
import json

from .models import EmployeeModel


# http://127.0.0.1:8000/first/message
def greet(request):
    return HttpResponse("hi employees good morning")


# http://127.0.0.1:8000/first/details
def get_details(request):
    return HttpResponse([
        {
            "id": "121",
            "name": "rahath",
            "email": "rahath@gmail.com",
            "phone": 1234567890,
            "address": "guntur",
            "designation": "phd",
            "emp_type": "developer",
            "salary": 25000
        }
    ])


@csrf_exempt
def add_employee(request):

    if request.method == "POST":

        data = json.loads(request.body)

        emp_data = EmployeeModel.objects.create(

            id=data.get("id"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address"),
            designation=data.get("designation"),
            emp_type=data.get("emp_type"),
            salary=data.get("salary")

        )

        return JsonResponse({

            "id": emp_data.id,
            "status": HTTPStatus.OK

        })

def get_employee_details(request):
    """
           this function is returning all the details of the employee table
           :param request:
           :return:

           """
    emp_data = EmployeeModel.objects.all().values()
    response_data=List(emp_data)
    return JsonResponse({
        "data":response_data,
        "status":HTTPStatus.OK,
    })

def get_emp_by_id(request, id):
    """
    this function takes id as input through url
    and return the data of that user
    :param request:
    :request:

    """
    emp_data = EmployeeModel.objects.filter(id=id)

    return JsonResponse({
        "id":emp_data.id,
        "name":emp_data.name,
        "email":emp_data.email,
        "phone":emp_data.phone,
        "designation":emp_data.designation,
        "emp_type":emp_data.emp_type,
        "employee_salary":emp_data.salary
    })