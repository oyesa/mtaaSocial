from django.shortcuts import render
from .models import *



# Create your views here.
def home(request):
  current_user=request.user
  profiles=Profile.objects.filter(id=current_user.id).all()
  return render(request, 'home.html')


def profile(request):
  current_user=request.user
  return render(request, 'profile.html')
