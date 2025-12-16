from django.http import JsonResponse
from .models import *

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


def exclude_data(request):
    # Exclude Data
    users = User.objects.exclude(username__icontains="ra").values()
    return JsonResponse({"user": list(users)})


def sort_ascending(request):
    #AscendingOrder
    users = User.objects.all().order_by("username").values()
    return JsonResponse({"user": list(users)})

def sort_descending(request):
    #Desanding Order
    users = User.objects.all().order_by("-username").values()
    return JsonResponse({"user": list(users)})


def limiting_data(request):
    #Limiting Data
    users = User.objects.all()[1:3].values()
    return JsonResponse({"user": list(users)})


    #Agrigation
from django.db.models import Avg, Max, Min, Sum, Count

def count_data(request):
    #count
    users = User.objects.aggregate(Count('id'))
    return JsonResponse({"user": users})

def max_data(request):
    #max
    users = User.objects.aggregate(Max('otp'))
    return JsonResponse({"user": users})

def min_data(request):
    #min
    users = User.objects.aggregate(Min('otp'))
    return JsonResponse({"user": users})

def avg_data(request):
    # avg
    users = User.objects.aggregate(Avg('otp'))
    return JsonResponse({"user": users})

def sum_data(request):
    #sum
    users = User.objects.aggregate(Sum('otp'))
    return JsonResponse({"user": users})

def aggregate_data(request):
    #Aggregation
    data = User.objects.aggregate(
        total_users=Count('id'),
        max_otp=Max('otp'),
        min_otp=Min('otp'),
        avg_otp=Avg('otp'),
        sum_otp=Sum('otp')
    )
    return JsonResponse({"user_statistics": data})


def insert_data(request):
    # #Insert Data
    user = User.objects.create(
        username="newuser",
        email="newuser@gmail.com",
        mobile="1234567890",
        password="password123",
        first_name="New",
        last_name="User",
        otp=123456
    )
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'mobile': user.mobile,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at,
        'updated_at': user.updated_at,
    })


def insert_multiple_data(request):
    # Insert Multiple Data
    users = [
        User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
             otp=123456),
        User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
             otp=123456),
        User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
             otp=123456),
        User(first_name="John", last_name="Doe", email="John@example.com", mobile="123456", password="123456",
             otp=123456),
    ]
    User.objects.bulk_create(users)
    return JsonResponse({"msg": "Bulk Created Successfully"})


def delete_data(request):
    #Delete Data
    User.objects.get(id=4).delete()
    return JsonResponse({"msg": "Deleted Successfully"})


def update_data(request):
    # Update data
    User.objects.filter(id=3).update(
        username='nazmul',
        password='nazmul',
        first_name='Nazmul',
        last_name='Islam',
        email='nazmul@gmail.com'
    )
    return JsonResponse({"msg": "Updated Successfully"})


#Comparison Operator
def equal_data(request):
    result = Product.objects.filter(price=500).values()
    return JsonResponse({"equal_data": list(result)})

def greater_then(request):
    result = Product.objects.filter(price__gt=500).values()
    return JsonResponse({"gt_data": list(result)})

def less_then(request):
    result = Product.objects.filter(price__lt=500).values()
    return JsonResponse({"less_data": list(result)})

def gt_equal(request):
    result = Product.objects.filter(price__gt=500).values()
    return JsonResponse({"gt_data": list(result)})

def lt_equal(request):
    result = Product.objects.filter(price__lt=500).values()
    return JsonResponse({"less_data": list(result)})


from  django.db.models import Q
def q_data(request):
    result = Product.objects.filter(
        Q(name="Apple") |
        Q(price__lt=500) |
        Q(price__gt=500)
    ).values()
    return JsonResponse({"cmb_data": list(result)})


def case_sens(request):
    result = Product.objects.filter(name__contains='pp').values()
    return JsonResponse({"Data": list(result)})

def case_notsens(request):
    result = Product.objects.filter(name__icontains='p').values()
    return JsonResponse({"Data": list(result)})

def start_with(request):
    result = Product.objects.filter(name__startswith='p').values()
    return JsonResponse({"Data": list(result)})

def end_with(request):
    result = Product.objects.filter(name__endswith='e').values()
    return JsonResponse({"Data": list(result)})