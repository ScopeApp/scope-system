from django.db import models
from django.contrib.auth.models import User;
from backend.students.models import Students, Subjects

class Assignments(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Students, models.CASCADE, db_column='studentid')
    # קישור ישיר ל-User במקום ל-UserProfile
    teacher = models.ForeignKey(User, models.CASCADE, db_column='teacherid')
    subjectid = models.ForeignKey(Subjects, models.CASCADE, db_column='subjectid')

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
