from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# auth_views: new in django 1.11 and up allows you to use LoginView and LogoutView without having to
# write the views for them

app_name = 'users'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
]