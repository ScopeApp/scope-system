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

class Assignments(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey('Students', models.CASCADE, db_column='studentid')
    # קישור ישיר ל-User במקום ל-UserProfile
    teacher = models.ForeignKey(User, models.CASCADE, db_column='teacherid')
    subjectid = models.ForeignKey('Subjects', models.CASCADE, db_column='subjectid')

    class Meta:
        managed = False
        db_table = 'assignments'

class Attachments(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    attachedtotype = models.CharField(max_length=20)
    attachedtoid = models.IntegerField()
    # קישור ישיר ל-User במקום ל-UserProfile
    reporter = models.ForeignKey(User, models.CASCADE, db_column='reporterid')
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
    # קישור ישיר ל-User במקום ל-UserProfile
    reporter = models.ForeignKey(User, models.CASCADE, db_column='reporterid')
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