from django.shortcuts import render
from .models import AccessLog

# Create your views here.
def introduce(request):
    if request.method == 'GET':
        user = request.user
        access = AccessLog()
        access.author = user
        access.location = 'introduce'
        access.created_at = AccessLog.created_at
        access.save()
        return render(request, 'introduce/introduce.html')
