from .models import *

def home(request):
    user =User.objects.get(id=1)