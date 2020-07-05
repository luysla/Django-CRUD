from django.db import models
from django.utils import timezone
from django.conf import settings

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def createTask(self):
        self.save()
    
    def __str__(self):
        return self.name