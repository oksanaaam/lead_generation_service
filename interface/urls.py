from django.urls import path
from . import views
from .views import deploying_page

app_name = "interface"

urlpatterns = [
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/signup/", views.signup_view, name="signup"),
    path("lead_generator/", views.lead_generator_view, name="lead_generator"),
    path("deploying/", deploying_page, name="deploying"),
]
