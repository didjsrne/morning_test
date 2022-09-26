from django.shortcuts import render

def introduce(request):
    if request.method =='GET':
        return render(request, 'introduce/introduce.html')
# Create your views here.
