from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('course', views.CourseListView.as_view(), name='courses') ,
    path('<int:pk>', views.CoursesDetailView.as_view(), name='course_detail'),

]
