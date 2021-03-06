# Generated by Django 3.0.8 on 2020-08-07 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_type', models.CharField(max_length=50)),
                ('host_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('host_port', models.IntegerField()),
                ('host_ip', models.GenericIPAddressField()),
                ('passwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HType',
            fields=[
                ('htype', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
