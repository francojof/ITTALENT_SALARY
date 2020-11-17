from django.contrib import admin
from django.urls import path
from formularioPersona import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/',views.index, name="formulario"),
    path('inicio/',views.inicio),
    path('post-json/',views.post_json, name='posts-json-view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)