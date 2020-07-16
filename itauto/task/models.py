from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    task_type = models.CharField(max_length=50)
    latest_status = models.CharField(max_length=50)
    create_time = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    update_time = models.CharField(max_length=50)

