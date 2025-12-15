from django.http import JsonResponse, HttpResponse
from .models import *

def home(request):
    return HttpResponse("Django ORM Query Filtering Agrigate Operation")

def fetch_alldata(request):
    #Fetch all user data
    users =User.objects.all().values()
    return JsonResponse({"user":list(users)})


def fetch_singledata(request):
    #Fetch single user data
    users =User.objects.get(id=1)
    return JsonResponse({"user":(users.username)})


def fetch_firstdata(request):
    #Fetch First Data
    users =User.objects.first()
    return JsonResponse({
        'id': users.id,
        'username': users.username,
        'email': users.email,
        'mobile': users.mobile,
        'first_name': users.first_name,
        'last_name': users.last_name,
        'created_at': users.created_at,
        'updated_at': users.updated_at,
    })


def fetch_lastdata(request):
    #Fetch Last Data
    users =User.objects.last()
    return JsonResponse({
        'id': users.id,
        'username': users.username,
        'email': users.email,
        'mobile': users.mobile,
        'first_name': users.first_name,
        'last_name': users.last_name,
        'created_at': users.created_at,
        'updated_at': users.updated_at,
    })


def filter_data(request):
    # Filtering Data
    users = User.objects.filter(username__icontains="ra").values()
    return JsonResponse({"user": list(users)})


    # Exclude Data
    # users = User.objects.exclude(username__icontains="ra").values()
    # return JsonResponse({"user": list(users)})


    #Sorting Data
    #Assanding Order
    # users = User.objects.all().order_by("username").values()
    # return JsonResponse({"user": list(users)})
    #Desanding Order
    # users = User.objects.all().order_by("-username").values()
    # return JsonResponse({"user": list(users)})


    #Limiting Data
    # users = User.objects.all()[1:3].values()
    # return JsonResponse({"user": list(users)})


    #Agrigation
    from django.db.models import Avg, Max, Min, Sum, Count

    #count
    # users = User.objects.aggregate(Count('id'))
    # return JsonResponse({"user": users})
    #max
    # users = User.objects.aggregate(Max('otp'))
    # return JsonResponse({"user": users})
    #min
    # users = User.objects.aggregate(Min('otp'))
    # return JsonResponse({"user": users})
    # avg
    # users = User.objects.aggregate(Avg('otp'))
    # return JsonResponse({"user": users})
    #sum
    # users = User.objects.aggregate(Sum('otp'))
    # return JsonResponse({"user": users})

    #Agrigation
    # data = User.objects.aggregate(
    #     total_users=Count('id'),
    #     max_otp=Max('otp'),
    #     min_otp=Min('otp'),
    #     avg_otp=Avg('otp'),
    #     sum_otp=Sum('otp')
    # )
    # return JsonResponse({"user_statistics": data})


    # #Insert Data
    # user = User.objects.create(
    #     username="newuser",
    #     email="newuser@gmail.com",
    #     mobile="1234567890",
    #     password="password123",
    #     first_name="New",
    #     last_name="User",
    #     otp=123456
    # )
    # return JsonResponse({
    #     'id': user.id,
    #     'username': user.username,
    #     'email': user.email,
    #     'mobile': user.mobile,
    #     'first_name': user.first_name,
    #     'last_name': user.last_name,
    #     'created_at': user.created_at,
    #     'updated_at': user.updated_at,
    # })

    # Insert Multiple Data
    # users = [
    #     User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
    #          otp=123456),
    #     User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
    #          otp=123456),
    #     User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
    #          otp=123456),
    #     User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
    #          otp=123456),
    # ]
    # User.objects.bulk_create(users)
    # return JsonResponse({"msg": "Bulk Created Successfully"})

    #Delete Data
    # User.objects.get(id=4).delete()
    # return JsonResponse({"msg": "Deleted Successfully"})

    # Update data
    # User.objects.filter(id=3).update(
    #     username='nazmul',
    #     password='nazmul',
    #     first_name='Nazmul',
    #     last_name='Islam',
    #     email='nazmul@gmail.com'
    # )
    #
    # return JsonResponse({"msg": "Updated Successfully"})

