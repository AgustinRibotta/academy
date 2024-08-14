from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    fname = models.CharField(_("First Name"), max_length=50)
    lname = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    date_of_birth = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return f"{self.fname} {self.lname}"
