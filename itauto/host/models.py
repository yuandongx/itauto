from django.db import models

class Hosts(models.Model):

    host_type = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    host_port = models.IntegerField()
    host_ip = models.GenericIPAddressField()
    passwd = models.CharField(max_length=50)

class HostType(models.Model):
    type_id = models.CharField(primary_key=True, max_length=110)
    host_type = models.CharField(max_length=50)
    host_sub_type = models.CharField(max_length=50)
