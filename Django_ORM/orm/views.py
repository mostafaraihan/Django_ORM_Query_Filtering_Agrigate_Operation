from django.http import JsonResponse
from .models import *

def home(request):

    #Fetch all user data
    users =User.objects.all().values()
    return JsonResponse({"user":list(users)})