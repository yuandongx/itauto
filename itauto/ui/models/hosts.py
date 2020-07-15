from django.db import models

class Host(models.Model):
    host_type = models.CharField()
    host_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    host_port = models.IntegerField()
    host_ip = models.IPAddressField()
    def __str__(self):
        return "host"