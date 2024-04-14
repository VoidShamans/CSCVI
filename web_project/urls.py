from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('Home/', views.home, name='home'),
    path('Video/', views.video, name='video'),
    path('Discussion/', views.discussion, name='discussion'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('sign_out/', views.sign_out, name='sign_out'),
]