from django.db import models
import uuid
# Create your models here.

class Task(models.Model):

    task_name = models.CharField(max_length=50)
    task_type = models.CharField(max_length=50)
    latest_status = models.CharField(max_length=50)
    create_time = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    update_time = models.CharField(max_length=50)
    task_uuid = models.UUIDField(primary_key=True,
                                 auto_created=True,
                                 default=uuid.uuid4,
                                 editable=False)
