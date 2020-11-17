from django.contrib import admin
from django.urls import path
from formularioPersona import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="IT_Talent_Salary"),
]