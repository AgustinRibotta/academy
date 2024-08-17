from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, TemplateView, CreateView
import markdown
from .models import Course, Enrollment
from apps.students.models import Student

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


@login_required
def enroll_now(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_id = request.user.id

    try:
        student = Student.objects.get(user_id=user_id)
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': "Student profile not found."})

    # Usar las instancias del modelo en lugar de IDs
    enrollment, created = Enrollment.objects.get_or_create(student_id=student, course_id=course)

    if created:
        message = "You have been enrolled in the course successfully."
    else:
        message = "You are already enrolled in this course."

    return render(request, 'course/enrollment_confirmation.html', {'message': message, 'course': course})


@login_required
def unenroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_id = request.user.id

    try:
        student = Student.objects.get(user_id=user_id)
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': "Student profile not found."})

    # Intenta obtener la inscripción del curso para el estudiante
    try:
        enrollment = Enrollment.objects.get(student_id=student, course_id=course)
        enrollment.delete()
        message = "You have been successfully unenrolled from the course."
    except Enrollment.DoesNotExist:
        message = "You are not enrolled in this course."

    return render(request, 'course/enrollment_confirmation.html', {'message': message, 'course': course})
