from django.db import models
from django.utils.translation import gettext_lazy as _


class Syllabus(models.Model):
    description = models.FileField(_("Syllabus"), upload_to='syllabus/', max_length=100)

class Course(models.Model):

    name = models.CharField(_("Course Name"), max_length=50)
    description = models.TextField(_("Course Description"))
    syllabu_id = models.ForeignKey("Syllabus", verbose_name=_("Sylabus"), on_delete=models.CASCADE)
