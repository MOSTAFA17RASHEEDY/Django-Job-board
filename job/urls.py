from xml.etree.ElementInclude import include
from django.urls import path, include
from job import views
app_name = 'job'
urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_details, name='job_details'),
]
