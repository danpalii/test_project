from django.urls import path

from users.views import login, register, log_out

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]