from django.conf import settings
from django.db import models
from django.utils import timezone

class SchoolDetail(models.Model):
    schoolname = models.CharField('School Name', max_length=255, unique=True)
    email = models.EmailField('Email Id', max_length=100)
    mobile = models.CharField('Mobile Number',max_length=15,null=True,blank=True)
    fax = models.CharField('Fax', max_length=255,null=True,blank=True)
    address = models.TextField('Address',blank=True, null=True)
    country = models.CharField('Country', max_length=100,default='India')
    state = models.CharField('State',max_length=52,default='Tamil Nadu')
    city = models.CharField('City',max_length=100,blank=True)
    zipcode = models.CharField('Zip Code',max_length=6,null=True,blank=True)
    website = models.URLField('Website URL',null=True,blank=True)
    affillicateno = models.CharField('School Affillicate Number', max_length=100)
    logo = models.FileField('School Logo',upload_to='documents/',blank=True)
    username = models.CharField('Username', max_length=50, unique=True)
    password = models.CharField('Password', max_length=50, null=True)
    usertype = models.CharField('User Type', max_length=50, default='admin')

    def __str__(self):
        return self.schoolname

class StudentDetail(models.Model):
	school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
	student_name = models.CharField('Student Name', max_length=255)
	register_number = models.CharField('Register Number', max_length=50, unique=True)
	admission_number = models.CharField('Admission Number', max_length=50, unique=True)
	date_of_admission = models.DateField('Date Of Admission',null=True,blank=True)
	emergency_number = models.CharField('Emergency Number', max_length=50,null=True,blank=True)
	date_of_birth = models.DateField('Date Of Birth', null=True)
	adhar_number = models.CharField('Adhar Number',max_length=50,null=True,blank=True)
	father_name = models.CharField('Father Name', max_length=255,null=True,blank=True)
	mother_name = models.CharField('Mother Name', max_length=255,null=True,blank=True)
	guardian_name = models.CharField('Guardian Name', max_length=255,null=True,blank=True)
	father_occupation = models.CharField('Father Occupation', max_length=255,null=True,blank=True)
	mother_occupation = models.CharField('Mother Occupation', max_length=255, null=True,blank=True)
	blood_group = models.CharField('Blood Group', max_length=25,null=True,blank=True)
	present_address = models.TextField('Present Address',null=True,blank=True)
	permanent_address = models.TextField('Permanent Address',null=True,blank=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State', max_length=100,default='Tamil Nadu')
	city = models.CharField('City', max_length=100,null=True,blank=True)
	religion = models.CharField('Religion', max_length=100,null=True,blank=True)
	caste = models.CharField('Caste', max_length=100,null=True,blank=True)
	Photo = models.FileField('Student Photo',upload_to='user_image/',null=True,blank=True)
	user_type = models.CharField(default='student',max_length=10)
	no_of_backlogs = models.IntegerField(null=True)
	def __str__(self):
		return self.student_name

MARITAL_STATUS = (
    ('','Select'),
    ('single', 'Single'),
    ('married','Married'),
)
class StaffDetail(models.Model):
    staff_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    staff_name = models.CharField('Staff Name', max_length=255)
    email = models.EmailField('Email Id', max_length=100,null=True,blank=True)
    mobile = models.CharField('Mobile Number',max_length=20)
    emergency_number = models.CharField('Emergency Number',max_length=20)
    date_of_birth = models.DateField('Date Of Birth',null=True,blank=True)
    date_of_joining = models.DateField('Date Of Joining',null=True,blank=True)
    adhar_number = models.CharField('Adhar Number',max_length=100,null=True,blank=True)
    degree =  models.CharField('Degree', max_length=255, null=True)
    designation = models.CharField('Designation', max_length=25)
    age = models.IntegerField('Age',null=True,blank=True)
    blood_group = models.CharField('Blood Group', max_length=25,null=True,blank=True)
    marital_status = models.CharField('Marital Status', max_length=15, choices=MARITAL_STATUS,null=True,blank=True)
    present_address = models.TextField('Present Address',null=True,blank=True)
    permanent_address = models.TextField('Permanent Address',null=True,blank=True)
    Photo = models.FileField('Staff Photo',upload_to='user_image/',null=True,blank=True)
    username = models.CharField('User Name', max_length=100, unique=True)
    password = models.CharField('Password',max_length=30)
    user_type = models.CharField(default='staff',max_length=12)

    def __str__(self):
        return self.staff_name

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    class_name = models.CharField('Class Name', max_length=50)
    academic_year = models.CharField('Academic Year', max_length=50,null=True)

    def __str__(self):
        return self.class_name

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    section_name = models.CharField('Section Name', max_length=50)

    def __str__(self):
        return self.section_name

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    exams = models.CharField('Exam Name', max_length=100)

    def __str__(self):
        return self.exams

class Subject(models.Model):
	subject_id = models.AutoField(primary_key=True)
	school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
	exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
	subject_name = models.CharField('Subject Name', max_length=100)

	def __str__(self):
		return self.subject_name
class SchoolSetting(models.Model):
    settings_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE)
    academic_year = models.CharField('Academic Year', max_length=10)
    pagination_count = models.IntegerField('Pagination Count')

    def __str__(self):
        return self.academic_year
class AssignSubjectTeacher(models.Model):
    assign_subject_teacher_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(StaffDetail, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    academic_year = models.CharField('Academic Year', max_length=20)
    is_class_teacher =  models.CharField('Class Teacher', max_length=10, default="no",null=True,blank=True)

    def __str__(self):
        return self.is_class_teacher

class StudentSection(models.Model):
	student_section_id = models.AutoField(primary_key=True)
	student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
	academic_year = models.CharField('Academic Year', max_length=20)
	reg_no = models.CharField(max_length=200,null=True)
	student_name = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.academic_year
class StudentLogin(models.Model):
	login_id = models.AutoField(primary_key=True)
	name = models.CharField('Name', max_length=100)
	reg_no = models.CharField('Register No', max_length=100)
	email = models.EmailField('Email Id', max_length=100)
	mobile = models.CharField('Mobile Number',max_length=15,null=True,blank=True)
	address = models.TextField('Address',blank=True, null=True)
	country = models.CharField('Country', max_length=100,default='India')
	state = models.CharField('State',max_length=52,default='Tamil Nadu')
	city = models.CharField('City',max_length=100,blank=True)
	username = models.CharField('Username', max_length=50, unique=True)
	password = models.CharField('Password', max_length=50, null=True)
	def __str__(self):
		return self.name
class Mark(models.Model):
	mark_id = models.AutoField(primary_key=True)
	student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE,null=True)
	class_id = models.IntegerField('Class Id',null=True,)
	section_id = models.IntegerField('Section Id',null=True,)
	subject_id = models.IntegerField('Subject Id',null=True,)
	mark_type =  models.CharField('Mark Type',null=True,max_length=100)
	mark = models.IntegerField('Mark',null=True)
	exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
	reg_no = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.student_id.student_name
class StudentDiary(models.Model):
    diary_id= models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(StaffDetail, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assigned_date= models.DateField('Assigned Date')
    diary_note = models.TextField('Dairy Notes')
    homework_classwork= models.IntegerField('Home Work/ Class Work',null=True)
    def __str__(self):
        return self.diary_note
class ParentsDetail(models.Model):
    student_id = models.ForeignKey(StudentSection, on_delete=models.CASCADE)
    school_id = models.ForeignKey(SchoolDetail,on_delete=models.CASCADE,null=True)
    register_number = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.username
class EventDetail(models.Model):
    school_id = models.ForeignKey(SchoolDetail,on_delete=models.CASCADE,null=True)
    event_name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    date = models.DateField()
    time = models.CharField(max_length=200)
    address= models.TextField(max_length=2000)
    def __str__(self):
        return self.event_name
class Meeting(models.Model):
    school_id = models.ForeignKey(SchoolDetail, on_delete=models.CASCADE,null=True)
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE,null=True)
    section_id = models.ForeignKey(Section,on_delete=models.CASCADE,null=True)
    staff_id = models.ForeignKey(StaffDetail,on_delete=models.CASCADE,null=True)
    time = models.CharField(max_length=200)
    msg = models.TextField(max_length=2000)
    date = models.DateField()
    def __str__(self):
        return self.msg
class Attendance(models.Model):
	student_id = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
	section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
	exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
	reg_no = models.CharField(max_length=200)
	total_days = models.CharField(max_length=200)
	no_of_days_present =  models.CharField(max_length=200)
	no_of_days_absent =  models.CharField(max_length=200)
	percentage = models.CharField(max_length=200)
	def __str__(self):
		return self.student_id.student_name
