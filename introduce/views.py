from django.shortcuts import render
from .models import AccessLog


# Create your views here.
def introduce(request):
    if request.method == 'GET':
        # case 1
        """
        access_log = AccessLog()
        access_log.location = "introduce"
        access_log.save()
        """
        # case 2
        AccessLog.objects.create(
            location="introduce"
        )

        return render(request, 'introduce/introduce.html')
