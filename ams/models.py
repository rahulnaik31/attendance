from django.db import models
from django.contrib.auth.models import User # to Create user
# import uuid # to Create unique user id
from django.urls import reverse

# Create your models here.

#branch

class Branch(models.Model):
    # branchId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branchId=models.AutoField(primary_key=True)
    BN = (
        ('Computer', 'Computer'),
        ('Mechanical', 'Mechanical'),
        ('Civil', 'Civil'),
        ('Electronics', 'Electronics'),
    )
    branchName=models.CharField(max_length=100, choices = BN, null = True, help_text = "Branch")

    def __str__(self):
        return self.branchName


#year
class AcademicYear(models.Model):
    # yearId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    yearId=models.AutoField(primary_key=True)
    yearName=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.yearName

#Semester
class Semester(models.Model):
    # semesterId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semesterId=models.AutoField(primary_key=True)
    semesterName=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.semesterName

#Subject
class Subject(models.Model):
    # subjectId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subjectId=models.AutoField(primary_key=True)
    subjectName=models.CharField(max_length=255)
    subjectShortName=models.CharField(max_length=255)
    branchId=models.ForeignKey(Branch, related_name="SubjectBranchId",null=False, blank=True,on_delete=models.CASCADE)
    semesterId=models.ForeignKey(Semester, related_name="SubjectSemesterId",null=False, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.subjectName


#Students Model
class Students(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollNo = models.IntegerField(primary_key=True)
    year = models.ForeignKey(AcademicYear, related_name="AcademicYearId",null=False,on_delete=models.CASCADE)
    semesterId=models.ForeignKey(Semester, related_name="StudentSemesterId",null=False,on_delete=models.CASCADE)
    branchId=models.ForeignKey(Branch, related_name="StudentBranchId",null=False,on_delete=models.CASCADE)
    SEX= (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        )
    gender =models.CharField(max_length=10, choices = SEX, null = True, help_text = "Gender")

    def __str__(self):
        return format(self.user.username)

    class Meta:
        ordering = ["-user"]
        permissions = (("is_student", "is_student"),)

    def get_absolute_url(self):
        return reverse('profile')

#faculty model
class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # facultyId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facultyId=models.AutoField(primary_key=True)
    branchId=models.ForeignKey(Branch, related_name="FacultyBranchId",null=False, blank=True,on_delete=models.CASCADE)
    SEX= (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender =models.CharField(max_length=10, choices = SEX, null = True, help_text = "Gender")

    class Meta:
        permissions = (('is_faculty', 'is_faculty'),) #try

    def __str__(self):
        return self.user.username


#SubjectByFaculty
class StudentByClass(models.Model):
    rollNo=models.OneToOneField(Students,on_delete=models.CASCADE,primary_key=True)
    semesterId=models.ForeignKey(Semester, related_name="StudentByClasssemesterId",null=False, blank=True,on_delete=models.CASCADE)
    branchId=models.ForeignKey(Branch, related_name="StudentByClassbranchId",null=False, blank=True,on_delete=models.CASCADE)

#SubjectByFaculty
class SubjectByFaculty(models.Model):
    # subjectByFacultyId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subjectByFacultyId=models.AutoField(primary_key=True)
    subjectId=models.ForeignKey(Subject, related_name="SubjectByFacultysubjectId",null=False, blank=True,on_delete=models.CASCADE)
    facultyId=models.ForeignKey(Faculty, related_name="SubjectByFacultyfacultyId",null=False, blank=True,on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse("home",kwargs={'pk':self.pk})


#Attendance
class Attendance(models.Model):
    # attendanceId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendanceId=models.AutoField(primary_key=True)
    studentByClassRollNo=models.ForeignKey(StudentByClass, related_name="AttendancestudentByClassId",null=False, blank=True,on_delete=models.CASCADE)
    subjectByFacultyId=models.ForeignKey(SubjectByFaculty, related_name="AttendancesubjectByFacultyId",null=False, blank=True,on_delete=models.CASCADE)
    semesterId=models.ForeignKey(Semester,related_name="AttendancesemesterId",null=False, blank=True,on_delete=models.CASCADE)
    branchId=models.ForeignKey(Branch,related_name="AttendancebranchId",null=False, blank=True,on_delete=models.CASCADE)
    attendance=models.BooleanField()
    date = models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
