from django.urls import path
from blog import views
from .views import  successView, Homepage

urlpatterns = [
    path('', Homepage, name='home'),
    path('blog/', views.post_list, name="post_list"),
    path('success/', successView, name='success'),
]