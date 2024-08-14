from django.db import models
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField

# Create your models here.

class Course(models.Model):

    name = models.TextField(_("Course Name"))
    description = models.TextField(_("Desciption"))
    syllabus = MarkdownxField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name

