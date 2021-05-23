from django.db import models


# Create your models here.

class AcademicYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    acd_year = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'academic_year'


class CourseAcademic(models.Model):
    course_id = models.CharField(max_length=100)
    year_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_academic'


class Department(models.Model):
    deptname = models.CharField(primary_key=True, max_length=100)
    hod = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class FacultyDesignation(models.Model):
    fid = models.ForeignKey('FacultyDetails', models.DO_NOTHING, db_column='fid')
    designation = models.TextField()

    class Meta:
        managed = False
        db_table = 'faculty_designation'


class FacultyDetails(models.Model):
    fid = models.CharField(primary_key=True, max_length=50)
    name = models.TextField()
    deptname = models.CharField(max_length=100)
    phoneno = models.TextField()
    email = models.TextField()
    photo = models.TextField()

    class Meta:
        managed = False
        db_table = 'faculty_details'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'