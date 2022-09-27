from django.contrib import admin
from .models import AccessLog  # introduce.models = 절대 경로 / .models = 상대 경로

# Register your models here.
admin.site.register(AccessLog)
