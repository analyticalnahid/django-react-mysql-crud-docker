from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department', views.departmentAPI),
    path('department/<int:id>', views.departmentAPI),
    
    path('employee', views.employeeAPI),
    path('employee/<int:id>', views.employeeAPI),
    
    path('employee/savefile', views.saveFile),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

