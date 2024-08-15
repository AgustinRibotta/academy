from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.views.generic import TemplateView
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