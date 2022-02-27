from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    register_number = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    admission_number = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_admission = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': "form-control"}))
    adhar_number = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    father_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    mother_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    guardian_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    father_occupation = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    mother_occupation = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    blood_group = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    present_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    permanent_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    country = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control","value":"India"}))
    state = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control","value":"TamilNadu"}))
    city = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    religion = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    caste = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    Photo = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = StudentDetail
        exclude  = ('user_type',)
        widgets={
            'password': forms.PasswordInput(attrs={'class': "form-control"}),
            
        }
class StudentEditForm(forms.ModelForm):
	student_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	register_number = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_number = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	date_of_admission = forms.DateField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control"}))
	date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': "form-control"}))
	adhar_number = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	father_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	mother_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	guardian_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	father_occupation = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	mother_occupation = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	blood_group = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	present_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
	permanent_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
	country = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control","value":"India"}))
	state = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control","value":"TamilNadu"}))
	city = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	caste = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
	Photo = forms.FileField(required=False,widget=forms.FileInput(attrs={'class': "form-control"}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'readonly': "readonly"}))
	password = forms.CharField(required=False)
	no_of_backlogs = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	class Meta:
		model = StudentDetail
		exclude  = ('user_type',)
		widgets={
			'password': forms.PasswordInput(attrs={'class': "form-control"}),
			
		}
class StaffForm(forms.ModelForm):
    staff_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_number = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_joining = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    adhar_number = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    degree =  forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    blood_group = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    present_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    permanent_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    bank_details = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    Photo = forms.CharField(required=False,widget=forms.FileInput(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = StaffDetail
        exclude  = ('user_type',)
        widgets={
            'password': forms.PasswordInput(attrs={'class': "form-control"}),
            'marital_status': forms.Select(attrs={'class': "form-control" }),
        }

class StaffEditForm(forms.ModelForm):
    staff_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_number = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_birth = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_joining = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    adhar_number = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    degree =  forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    blood_group = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    present_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    permanent_address = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'readonly': "readonly"}))

    class Meta:
        model = StaffDetail
        exclude  = ('user_type',)
        fields = ('staff_name', 'email','mobile','emergency_number',
            'adhar_number','degree','designation','age','blood_group','present_address','permanent_address','username',)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields =  '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('school_id', 'class_id','section_id','exams',)
        widgets={
            'exams': forms.TextInput(attrs={'class': "form-control"}),
            'school_id': forms.Select(attrs={'class': "form-control" }),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }
class ExamEditForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('school_id', 'class_id','section_id','exams',)
        widgets={
            'exams': forms.TextInput(attrs={'class': "form-control"}),
            'school_id': forms.Select(attrs={'class': "form-control" }),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('class_id', 'school_id','section_id','subject_name',)
        widgets={
            'subject_name': forms.TextInput(attrs={'class': "form-control"}),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }
class SubjectEditForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('class_id', 'school_id','section_id','subject_name',)
        widgets={
            'subject_name': forms.TextInput(attrs={'class': "form-control"}),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }
class AssignTeacherForm(forms.ModelForm):
    class Meta:
        model = AssignSubjectTeacher
        fields = ('staff_id', 'class_id','section_id','subject_id','academic_year','is_class_teacher',)
        widgets={
            'academic_year': forms.TextInput(attrs={'class': "form-control"}),
            'staff_id': forms.Select(attrs={'class': "form-control" }),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
            'subject_id': forms.Select(attrs={'class': "form-control" }),
        }
class AssignTeacherEditForm(forms.ModelForm):
    class Meta:
        model = AssignSubjectTeacher
        fields = ('staff_id', 'class_id','section_id','subject_id','academic_year','is_class_teacher',)
        widgets={
            'academic_year': forms.TextInput(attrs={'class': "form-control"}),
            'staff_id': forms.Select(attrs={'class': "form-control" }),
            'class_id': forms.Select(attrs={'class': "form-control" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
            'subject_id': forms.Select(attrs={'class': "form-control" }),
        }

class StudentSectionForm(forms.ModelForm):
    class Meta:
        model = StudentSection
        fields = ('student_id', 'class_id','section_id','academic_year',)
        widgets={
            'academic_year': forms.TextInput(attrs={'class': "form-control"}),
            'student_id': forms.Select(attrs={'class': "form-control",'id' : "student_section_student_id" }),
            'class_id': forms.Select(attrs={'class': "form-control" , 'id' : "student_section_class" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }
class StudentSectionEditForm(forms.ModelForm):
    class Meta:
        model = StudentSection
        fields = ('student_id', 'class_id','section_id','academic_year',)
        widgets={
            'academic_year': forms.TextInput(attrs={'class': "form-control"}),
            'student_id': forms.Select(attrs={'class': "form-control",'id' : "student_section_student_id" }),
            'class_id': forms.Select(attrs={'class': "form-control" , 'id' : "student_section_class" }),
            'section_id': forms.Select(attrs={'class': "form-control" }),
        }
