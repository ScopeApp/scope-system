# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assignments(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey('Students', models.CASCADE, db_column='studentid')
    teacherid = models.ForeignKey('Users', models.CASCADE, db_column='teacherid')
    subjectid = models.ForeignKey('Subjects', models.CASCADE, db_column='subjectid')

    class Meta:
        managed = False
        db_table = 'assignments'


class Attachments(models.Model):
    attachmentid = models.AutoField(primary_key=True)
    attachedtotype = models.CharField(max_length=20)
    attachedtoid = models.IntegerField()
    reporterid = models.ForeignKey('Users', models.CASCADE, db_column='reporterid')
    filepath = models.CharField(max_length=255)
    uploaddate = models.DateTimeField()
    relevantdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'attachments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser,models.CASCADE)
    group = models.ForeignKey(AuthGroup,models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission,models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classes(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'classes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Progressupdates(models.Model):
    updateid = models.AutoField(primary_key=True)
    assignmentid = models.ForeignKey(Assignments,models.CASCADE, db_column='assignmentid')
    reporterid = models.ForeignKey('Users', models.CASCADE, db_column='reporterid')
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


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    tz = models.CharField(unique=True, max_length=10)
    fullname = models.CharField(max_length=100)
    userrole = models.CharField(max_length=20)
    passwordhash = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
