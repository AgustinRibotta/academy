from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LoginView, LogoutView, StudentUpdateView, UserDeleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/', UserDeleteView.as_view(), name='user_delete'),
    # Rutas para el CRUD de estudiantes
]
