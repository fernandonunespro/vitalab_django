from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/usuarios/cadastro/')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('exames/', include('exames.urls')),
    path('empresarial/', include('empresarial.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
