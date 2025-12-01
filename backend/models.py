# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User;

class Assignments(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey('Students', models.CASCADE, db_column='studentid')
    teacherid = models.ForeignKey(User, models.CASCADE, db_column='teacherid')
    subjectid = models.ForeignKey('Subjects', models.CASCADE, db_column='subjectid')

    class Meta:
        managed = False
        db_table = 'assignments'

class Attachments(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    attachedtotype = models.CharField(max_length=20)
    attachedtoid = models.IntegerField()
    reporterid = models.ForeignKey(User, models.CASCADE, db_column='reporterid')
    filepath = models.CharField(max_length=255)
    uploaddate = models.DateTimeField()
    relevantdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'attachments'


class Classes(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'classes'

class Progressupdates(models.Model):
    updateid = models.AutoField(primary_key=True)
    assignmentid = models.ForeignKey(Assignments,models.CASCADE, db_column='assignmentid')
    reporterid = models.ForeignKey(User, models.CASCADE, db_column='reporterid')
    reportdate = models.DateField()
    descriptiveupdate = models.TextField()

    class Meta:
        managed = False
        db_table = 'progressupdates'


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


class Subjects(models.Model):
    subjectid = models.AutoField(primary_key=True)
    subjectname = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'subjects'


class UserProfile(models.Model):
    userid=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    tz = models.CharField(unique=True, max_length=10)
    userrole = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
