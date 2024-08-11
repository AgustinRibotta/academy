from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Subjects(models.Model):
    teachers = models.ManyToManyField("teacher.Teacher", verbose_name=_("Teachers"))
    courses = models.ManyToManyField("courses.Course", verbose_name=_("Courses"))
    students = models.ManyToManyField("student.Student", verbose_name=_("Students"))
