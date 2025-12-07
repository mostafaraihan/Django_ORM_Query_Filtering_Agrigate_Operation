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
    users = User.objects.exclude(username__icontains="ra").values()
    return JsonResponse({"user": list(users)})