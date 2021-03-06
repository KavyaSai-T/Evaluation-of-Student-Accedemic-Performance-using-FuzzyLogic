from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.list import ListView

urlpatterns = [
	path('school/dashboard', views.dashboard, name='dashboard'),
    path('admin_login/', views.adminlogin, name='adminlogin'),
	path('profile/', views.profile, name='profile'),
    path('teachers/logout/', views.teacher_logout, name='teacher_logout'),
    path('logout/', views.logout, name='logout'),
    path('students/logout/', views.student_logout, name='student_logout'),
    path('school/teachers/add_teacher', views.add_teacher, name='add_teacher'),
    path('school/teachers', views.teachers, name='teachers'),
    path('school/students/add_student', views.add_student, name='add_student'),
    path('teachers/', views.teacher_login, name='teacher_login'),
    path('students/', views.student_login, name='student_login'),
    path('school/teacher/dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('school/student/dashboard', views.student_dashboard, name='student_dashboard'),
    path('school/students', views.students, name='students'),
    path('school/class/add_class_section', views.add_class_section, name='add_class_section'),
    path('school/class/edit_classes_sections/<int:cls_id>/<int:sec_id>/', views.edit_classes_sections, name='edit_classes_sections'),
    path('school/class/delete_classes_sections/<int:cls_id>/<int:sec_id>/', views.delete_classes_sections, name='delete_classes_sections'),
    path('school/class/edit_class/<int:cls_id>/', views.edit_class, name='edit_class'),
    path('school/class/delete_class/<int:cls_id>/', views.delete_class, name='delete_class'),
    path('school/subjects/add_subject', views.add_subject, name='add_subject'),
    path('school/teachers/assign_subjects_to_teachers', views.assign_subjects_to_teachers, name='assign_subjects_to_teachers'),
    path('school/exams/add_exam', views.add_exam, name='add_exam'),
    path('school/exams/edit_exam/<int:pk>', views.edit_exam, name='edit_exam'),
    path('school/settings/pagination_count', views.pagination_count, name='pagination_count'),
    path('school/change_password', views.admin_change_password, name='admin_change_password'),
    path('school/teacher/other_settings', views.pagination_count_year, name='pagination_count_year'),
    url(r'^ajax/select_academic_year/$', views.select_academic_year, name='select_academic_year'),
    path('school/student/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('school/student/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('school/student/student_section/', views.student_section, name='student_section'),
    path('school/student/student_mark/', views.student_mark, name='student_mark'),
    path('school/teacher/edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('school/teacher/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    path('school/student/mark/student_view_marks', views.student_view_marks, name='student_view_marks'),
    path('school/student/student_view_diary_notes', views.student_view_diary_notes, name='student_view_diary_notes'),
    url(r'^ajax/subject/$', views.select_section, name='select_section'),
	url(r'^ajax/exam/$', views.select_exam_college, name='select_exam_college'),
    path('school/edit_subject/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('school/delete_subject/<int:pk>/', views.delete_subject, name='delete_subject'),
    url(r'^ajax/select_class/$', views.select_class, name='select_class'),
    path('school/delete_exam/<int:pk>/', views.delete_exam, name='delete_exam'),
    url(r'^ajax/select_teacher_section/$', views.select_teacher_section, name='select_teacher_section'),
    url(r'^ajax/select_school_details/$', views.select_school_details, name='select_school_details'),
    url(r'^ajax/ajax_subject_count/$', views.ajax_subject_count, name='ajax_subject_count'),
    path('school/teacher/marks/manage_student_marks/', views.manage_student_marks, name='manage_student_marks'),
    path('school/teacher/marks/view_manage_student_marks/', views.view_manage_student_marks, name='view_manage_student_marks'),
    path('school/teacher/add_student_marks/<int:cls_id>/<int:sec_id>/<int:exam_id>/', views.add_student_marks, name='add_student_marks'),
    url(r'^ajax/ajax_student_marks/$', views.ajax_student_marks, name='ajax_student_marks'),
    path('school/teacher/manage_students_marks/', views.manage_students_marks, name='manage_students_marks'),
    path('school/teacher/add_student_diary_notes/', views.add_student_diary_notes, name='add_student_diary_notes'),
    path('school/teacher/diary/view_student_diary_notes', views.view_student_diary_notes, name='view_student_diary_notes'),
    path('school/teacher/is_class_teacher', views.is_class_teacher, name='is_class_teacher'),
    path('school/teacher/marks/class_student_mark_details/<int:class_id>/<int:section_id>/<int:exam_id>/', views.class_student_mark_details, name='class_student_mark_details'),
    path('school/teacher/exams/select_class_exam/', views.select_class_exam, name='select_class_exam'),
    path('school/teacher/students/assign_student_class/', views.assign_student_class, name='assign_student_class'),
    path('school/teacher/class/class_details/', views.class_details, name='class_details'),
    path('school/teacher/students/teacher_view_student_section/', views.teacher_view_student_section, name='teacher_view_student_section'),
    path('school/teacher/students/teacher_edit_student_section/<int:pk>/', views.teacher_edit_student_section, name='teacher_edit_student_section'),
    path('school/teacher/students/teacher_delete_student_section/<int:pk>/', views.teacher_delete_student_section, name='teacher_delete_student_section'),

    path('school/teacher/teacher_change_password', views.teacher_change_password, name='teacher_change_password'),
    path('school/students/view_student_section', views.view_student_section, name='view_student_section'),
    url(r'^ajax/select_academic_year/$', views.select_academic_year, name='select_academic_year'),
    url(r'^ajax/teacher/section_selection_student/$', views.section_selection_student, name='section_selection_student'),
    path('school/teacher/delete_student_section/<int:pk>/', views.delete_student_section, name='delete_student_section'),
    path('school/teacher/edit_student_section/<int:pk>/', views.edit_student_section, name='edit_student_section'),
    url(r'^ajax/select_subject/$', views.select_subject, name='select_subject'),
    path('school/teachers/assign_teachers_view/', views.assign_teachers_view, name='assign_teachers_view'),
    path('school/teachers/delete_assign_teacher/<int:pk>/', views.delete_assign_teacher, name='delete_assign_teacher'),
    path('school/teachers/edit_assign_teachers/<int:pk>/', views.edit_assign_subjects_to_teachers, name='edit_assign_subjects_to_teachers'),
    path('school/teacher/mark/import_mark/<int:class_id>/<int:section_id>/<int:exam_id>/', views.import_mark, name='import_mark'),
   
    url(r'^ajax/ajax_student_grap/$', views.ajax_student_grap, name='ajax_student_grap'),
    path('school/teacher/single_student_subject_marks_chart/<str:pk>/', views.single_student_subject_marks_chart, name='single_student_subject_marks_chart'),
    path('school/teacher/edit_students_mark/<str:pk>/', views.edit_students_mark, name='edit_students_mark'),
    path('school/teacher/exam/manage_exam_mark_chart/', views.manage_exam_mark_chart, name='manage_exam_mark_chart'),
    path('school/teacher/exam/particular_exam_mark_chart/<str:pk>/<int:cls_id>/<int:sec_id>/', views.particular_exam_mark_chart, name='particular_exam_mark_chart'),
    path('school/student/exam/Student_particular_exam_mark_chart/<str:pk>/<int:cls_id>/<int:sec_id>/', views.Student_particular_exam_mark_chart, name='Student_particular_exam_mark_chart'),
    path('school/teacher/teacher_class_diary/', views.teacher_class_diary, name='teacher_class_diary'),
    url(r'^ajax/select_exam/$', views.select_exam, name='select_exam'),
    path('school/student/mark/student_subject_marks_chart/<str:pk>/', views.student_subject_marks_chart, name='student_subject_marks_chart'),
    url(r'^ajax/ajax_exam_class_search/$', views.ajax_exam_class_search, name='ajax_exam_class_search'),
    url(r'^ajax/select_school_exam/$', views.select_school_exam, name='select_school_exam'),
    url(r'^ajax/search_student_marks_ajax/$', views.search_student_marks_ajax, name='search_student_marks_ajax'),
    url(r'^ajax/student_section_class_select/$', views.student_section_class_select, name='student_section_class_select'),
    path('school/teacher/marks/student_class_mark/<int:class_id>/<int:section_id>/<int:exam_id>/', views.student_class_mark, name='student_class_mark'),
    url(r'^ajax/mark_already_exist/$', views.mark_already_exist, name='mark_already_exist'),
    path('school/teacher/exam/choose_exam', views.choose_exam, name='choose_exam'),
    path('school/teacher/exam/select_exams', views.select_exams, name='select_exams'),
    url(r'^ajax/mark_ajax/$', views.mark_ajax, name='mark_ajax'),
    url(r'^ajax/teacher_mark_ajax/$', views.teacher_mark_ajax, name='teacher_mark_ajax'),
    url(r'^ajax/delete_mark/$', views.delete_mark, name='delete_mark'),
    path('school/student/mark/view_student_mark/', views.view_student_mark, name='view_student_mark'),
    url(r'^ajax/exam_list/$', views.exam_list, name='exam_list'),
    url(r'^ajax/get_exam_name/$', views.get_exam_name, name='get_exam_name'),
    path('school/student/marks/view_single_student_particular_exam_mark/', views.view_single_student_particular_exam_mark, name='view_single_student_particular_exam_mark'),
    path('school/teacher/chart/exam_mark_chart/<int:cls_id>/<int:sec_id>/<str:pk>/', views.exam_mark_chart, name='exam_mark_chart'),
    path('school/teacher/chart/exam_chart/<int:cls_id>/<int:sec_id>/<int:exam_id>/<str:stud_id>/', views.exam_chart, name='exam_chart'),
    url(r'^ajax/sub_ajax/$', views.sub_ajax, name='sub_ajax'),
    path('school/teacher/exam/select_exam_excel/', views.select_exam_excel, name='select_exam_excel'),
    url(r'^export/xlsx/$', views.export_subject_to_xlsx, name='export_subject_to_xlsx'),
    path('school/student/exam/single_student_exam_mark_chart/<int:cls_id>/<int:sec_id>/<str:pk>/', views.single_student_exam_mark_chart, name='single_student_exam_mark_chart'),
    path('school/student/chart/particular_exam_chart/<int:cls_id>/<int:sec_id>/<int:exam_id>/<str:stud_id>/', views.particular_exam_chart, name='particular_exam_chart'),
    url(r'^ajax/ajax_search_particular_student_mark/$', views.ajax_search_particular_student_mark, name='ajax_search_particular_student_mark'),
    url(r'^ajax/ajax_search_all_student_mark/$', views.ajax_search_all_student_mark, name='ajax_search_all_student_mark'),
    path('school/teachers/test_teacher/', views.test_teacher, name='test_teacher'),
    url(r'^ajax/ajax_exam_class_year_search/$', views.ajax_exam_class_year_search, name='ajax_exam_class_year_search'),
    path('school/teacher/search/search_student_year', views.search_student_year, name='search_student_year'),
    url(r'^ajax/ajax_exam_class_select_section/$', views.ajax_exam_class_select_section, name='ajax_exam_class_select_section'),
    path('school/teacher/students/chart/student_mark_yearly_chart/', views.student_mark_yearly_chart, name='student_mark_yearly_chart'),
    url(r'^ajax/sub_ajax_search_mark/$', views.sub_ajax_search_mark, name='sub_ajax_search_mark'),
    path('school/teacher/students/chart/student_mark_overall_yearly_chart/', views.student_mark_overall_yearly_chart, name='student_mark_overall_yearly_chart'),
    path('school/teacher/students/mark/manage_single_student_particular_exam_mark/', views.manage_single_student_particular_exam_mark, name='manage_single_student_particular_exam_mark'),
    path('schools/parents', views.add_parents, name='add_parents'),
    path('schools/events', views.add_events, name='add_events'),
    path('schools/delete_event/<int:pk>/', views.delete_event, name='delete_event'),
    path('schools/delete_parent/<int:pk>/', views.delete_parent, name='delete_parent'),
	path('studentedit/<int:pk>/', views.studentedit, name='studentedit'),
    path('schools/teacher/send_meeting', views.send_meeting, name='send_meeting'),
    path('schools/teacher/delete_meeting/<int:pk>/', views.delete_meeting, name='delete_meeting'),
    path('parents', views.parent_login, name='parent_login'),
    path('schools/parent/parent_dashboard', views.parent_dashboard, name='parent_dashboard'),
    path('schools/parent/parent_logout', views.parent_logout, name='parent_logout'),
    path('schools/parent/view_student_mark_parent', views.view_student_mark_parent, name='view_student_mark_parent'),
    path('schools/parent/metting_detail/<int:cid>/<int:sid>/', views.metting_detail, name='metting_detail'),
    path('schools/teacher/event_details_teacher', views.event_details_teacher, name='event_details_teacher'),
    path('schools/student/event_details_student', views.event_details_student, name='event_details_student'),
    path('schools/parent/event_details_parent', views.event_details_parent, name='event_details_parent'),
	path('admin_class/', views.admin_class, name='admin_class'),
	path('calculate_performance/', views.calculate_performance, name='calculate_performance'),
	path('view_exam/<int:cls_id>/<int:sec_id>/', views.view_exam, name='view_exam'),
	path('view_all_students/<int:cls_id>/<int:sec_id>/<int:pk>/', views.view_all_students, name='view_all_students'),
	path('add_subject_mark/<int:cls_id>/<int:sec_id>/<int:pk>/', views.add_subject_mark, name='add_subject_mark'),
	path('view_subject_mark/<int:cls_id>/<int:sec_id>/<int:pk>/', views.view_subject_mark, name='view_subject_mark'),
	path('view_subject_exmark/<int:cls_id>/<int:sec_id>/<int:pk>/', views.view_subject_exmark, name='view_subject_exmark'),
	path('student_list/<int:cls_id>/<int:sec_id>/<int:pk>/', views.student_list, name='student_list'),
	path('view_attendance/<int:pk>/', views.view_attendance, name='view_attendance'),
	path('view_average/<int:cls_id>/<int:sec_id>/<int:pk>/', views.view_average, name='view_average'),
	path('single/', views.single, name='single'),
	path('register/', views.register, name='register'),
	path('', views.landing_page, name='landing_page'),
	path('sexam/<int:cls_id>/<int:sec_id>/<int:pk>/', views.sexam, name='sexam'),
	path('view_all/<int:cls_id>/<int:sec_id>/<int:pk>/<int:stud_id>/', views.view_all, name='view_all'),
	path('exportcsv', views.exportcsv, name='exportcsv'),
]	
