from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('course', views.CourseListView.as_view(), name='courses') ,
     path('courses/search/', views.CourseSearchView.as_view(), name='course_search'),
    path('<int:pk>', views.CoursesDetailView.as_view(), name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_now, name='enroll_now'),
    path('unenroll/<int:course_id>/', views.unenroll, name='unenroll'),
    path('inscripciones/', views.list_enroll, name='list_enroll'),
]
