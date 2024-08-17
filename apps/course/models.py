from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.students.models import Student
# Create your models here.

class Course(models.Model):

    name = models.TextField(_("Course Name"))
    description = models.TextField(_("Desciption"))
    syllabus = models.TextField(_("Syllabus"))
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name


class Enrollment(models.Model):

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_data = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")

