from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, TemplateView, View
import markdown
from .models import Course, Enrollment
from apps.students.models import Student
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()[:4]
        return context
    
    
class CourseSearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        courses = Course.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        results = list(courses.values('id', 'name', 'description'))
        return JsonResponse({'results': results})
    

class CourseListView(ListView):
    model = Course
    template_name = "course/course.html"
    context_object_name = "courses"
    paginate_by = 10

    def get_queryset(self):
        queryset = Course.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class CoursesDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context['course']
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

    # Get or create the enrollment for the current course
    enrollment, created = Enrollment.objects.get_or_create(student_id=student, course_id=course)

    if created:
        message = "You have been enrolled in the course successfully."
    else:
        message = "You are already enrolled in this course."

    # Retrieve all enrollments for the student
    all_enrollments = Enrollment.objects.filter(student_id=student)

    return render(request, 'course/enrollment_confirmation.html', {
        'message': message,
        'course': course,
        'enroll': enrollment,
        'all_enrollments': all_enrollments
    })

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


@login_required
def list_enroll(request):
    user_id = request.user.id

    try:
        student = Student.objects.get(user_id=user_id)
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': "Perfil de estudiante no encontrado."})

    
    enrollments = Enrollment.objects.filter(student_id=student)

    if request.method == "POST":
        
        course_id = request.POST.get('course_id')
        try:
            enrollment = Enrollment.objects.get(student_id=student, course_id=course_id)
            enrollment.delete()
            message = "Te has desinscrito exitosamente del curso."
        except Enrollment.DoesNotExist:
            message = "No estás inscrito en este curso."
    else:
        message = None

    return render(request, 'student/enrollment_list.html', {
        'message': message,
        'enrollments': enrollments
    })