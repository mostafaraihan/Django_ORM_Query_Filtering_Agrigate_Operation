from django.http import JsonResponse
from .models import *

def home(request):

    #Fetch all user data
    # users =User.objects.all().values()
    # return JsonResponse({"user":list(users)})

    #Fetch single user data
    # users =User.objects.get(id=1)
    # return JsonResponse({"user":(users.username)})

    #Fetch Fist Data
    # users =User.objects.first()
    # return JsonResponse({
    #     'id': users.id,
    #     'username': users.username,
    #     'email': users.email,
    #     'mobile': users.mobile,
    #     'first_name': users.first_name,
    #     'last_name': users.last_name,
    #     'created_at': users.created_at,
    #     'updated_at': users.updated_at,
    # })

    #Fetch Last Data
    # users =User.objects.last()
    # return JsonResponse({
    #     'id': users.id,
    #     'username': users.username,
    #     'email': users.email,
    #     'mobile': users.mobile,
    #     'first_name': users.first_name,
    #     'last_name': users.last_name,
    #     'created_at': users.created_at,
    #     'updated_at': users.updated_at,
    # })


    # Filtering Data
    # users = User.objects.filter(username__icontains="ra").values()
    # return JsonResponse({"user": list(users)})


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
    data = User.objects.aggregate(
        total_users=Count('id'),
        max_otp=Max('otp'),
        min_otp=Min('otp'),
        avg_otp=Avg('otp'),
        sum_otp=Sum('otp')
    )
    return JsonResponse({"user_statistics": data})