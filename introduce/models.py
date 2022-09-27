from django.db import models

# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = "accesslog"

    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=256)