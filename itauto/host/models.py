from django.db import models

class Hosts(models.Model):
    host_type = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    host_port = models.IntegerField()
    host_ip = models.GenericIPAddressField()
    passwd = models.CharField(max_length=50)
