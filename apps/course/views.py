from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
import markdown
from .models import Course


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()[:4]
        return context




class CourseListView(ListView):
    model = Course
    template_name = "course/course.html"
    context_object_name = "courses"
    paginate_by = 10

    def get_queryset(self):
        return Course.objects.all()


class CoursesDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context['course']
        # Convertir el contenido Markdown a HTML
        course.syllabus_html = markdown.markdown(course.syllabus, extensions=['extra'])
        return context
