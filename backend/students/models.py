from django.db import models
class Students(models.Model):
    studentid = models.AutoField(primary_key=True)
    studenttz = models.CharField(unique=True, max_length=10)
    classid = models.ForeignKey(Classes,models.CASCADE, db_column='classid')
    yearid = models.CharField(max_length=4)
    interventionstatus = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    fathername = models.CharField(max_length=100, blank=True, null=True)
    mothername = models.CharField(max_length=100, blank=True, null=True)
    fatherphone = models.CharField(max_length=15, blank=True, null=True)
    motherphone = models.CharField(max_length=15, blank=True, null=True)
    fatheroccupation = models.CharField(max_length=100, blank=True, null=True)
    motheroccupation = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'
# Create your models here.

class Subjects(models.Model):
    subjectid = models.AutoField(primary_key=True)
    subjectname = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'subjects'


class Classes(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'classes'
