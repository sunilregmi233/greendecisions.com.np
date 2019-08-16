from django.urls import path
from Document.views import model_form_upload
from Document import views

urlpatterns = [
    path('', views.model_form_upload, name="model_form_upload"),
    
]