from django.db import models

# Create your models here.
class Courses(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    course_name = models.CharField(db_column='course_name', max_length=256)
    course_code = models.CharField(db_column='course_code', max_length=256)
    credits = models.IntegerField(db_column='credits')
    is_live = models.IntegerField(db_column ='is_live' ,blank=True, null=True)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'Courses'
        managed = True
        db_table = 'courses'

class Quizes(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    quiz_name = models.CharField(db_column='quiz_name', max_length=256)
    quiz_code = models.CharField(db_column='quiz_code', max_length=256)
    course_code = models.CharField(db_column='course_code', max_length=256)
    questions = models.JSONField(db_column ='questions' ,blank=True, null=True)
    max_marks = models.IntegerField(db_column='max_marks')
    passing_marks = models.IntegerField(db_column ='passing_marks' ,blank=True, null=True)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'Quizes'
        managed = True
        db_table = 'quizes'


class TeacherDetails(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    teacher_name = models.CharField(db_column='teacher_name', max_length=256)
    staff_id = models.CharField(db_column='staff_id', max_length=256)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'TeacherDetails'
        managed = True
        db_table = 'teacher_details'


class StudentDetails(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    student_name = models.CharField(db_column='student_name', max_length=256)
    registration_id = models.CharField(db_column='registration_id', max_length=256)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'StudentDetails'
        managed = True
        db_table = 'student_details'


class StudentQuiz(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    student_name = models.CharField(db_column='student_name', max_length=256)
    registration_id = models.CharField(db_column='registration_id', max_length=256)
    quiz_code = models.CharField(db_column='quiz_code', max_length=256)
    course_code = models.CharField(db_column='course_code', max_length=256)
    max_marks = models.IntegerField(db_column='max_marks')
    marks_obtained = models.IntegerField(db_column ='marks_obtained' ,blank=True, null=True)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'StudentQuiz'
        managed = True
        db_table = 'student_quiz'


class CourseStudentMarks(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    course_code = models.CharField(db_column='course_code', max_length=256)
    course_name = models.CharField(db_column='course_name', max_length=256)
    student_name = models.CharField(db_column='student_name', max_length=256)
    registration_id = models.CharField(db_column='registration_id', max_length=256)
    max_marks = models.IntegerField(db_column='max_marks')
    marks_obtained = models.IntegerField(db_column ='marks_obtained' ,blank=True, null=True)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(db_column='updated_at', auto_now=True)


    class Meta:
        verbose_name = 'CourseStudentMarks'
        managed = True
        db_table = 'course_student_marks'