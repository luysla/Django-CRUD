from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('taskapp.urls')),
    path('admin/', admin.site.urls),
]
