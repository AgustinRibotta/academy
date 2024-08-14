from django.contrib import admin
from markdownx.widgets import MarkdownxWidget
from markdownx.models import MarkdownxField
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': MarkdownxWidget},
    }

admin.site.register(Course, CourseAdmin)