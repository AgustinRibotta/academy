from django.db import models
from django.utils.translation import gettext_lazy as _

class Teacher(models.Model):

    fname = models.CharField(_("First Name"), max_length=50)
    lname = models.CharField(_("Last Name"), max_length=50)
    username =  models.CharField(_("User Name"), max_length=50)
    password =  models.TextField(_("Passowrd"))
    

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return self.name

