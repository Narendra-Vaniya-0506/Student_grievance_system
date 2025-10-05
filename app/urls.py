from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("register_grievance", views.register_grievance, name="register_grievance"),
    path("track_grievance", views.track_grievance, name="track_grievance"),
    path("report_a_problem", views.report_a_problem, name="report_a_problem"),
    path("get_more_help", views.get_more_help, name="get_more_help"),
    path("grievance_detail/<int:ref_no>", views.grievance_detail, name="grievance_detail"),
    path("handler_response/<int:ref_no>", views.handler_response, name="handler_response"),
    path("satisfied_fn/<int:ref_no>", views.satisfied_fn, name="satisfied_fn"),
]