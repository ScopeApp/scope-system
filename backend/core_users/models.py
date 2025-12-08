from django.db import models
from django.contrib.auth.models import User;

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column='userid',
        primary_key=True
    )
    tz = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'users'
# Create your models here.
