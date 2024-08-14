from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Course

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()[:4]  # Obtener los primeros 4 cursos
        return context
    



class CourseListView(ListView):
    model = Course
    template_name = "course/course.html"  # Nombre del template
    context_object_name = "courses"      # Nombre del contexto en el template
    paginate_by = 10                    # Número de cursos por página

    def get_queryset(self):
        return Course.objects.all()