from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):

    fname = models.CharField(_("Firts Name"), max_length=50)
    lname = models.CharField(_("Last Name"), max_length=50)
    username = models.TextField(_("User Name"))
    password = models.TextField(_("Password"))