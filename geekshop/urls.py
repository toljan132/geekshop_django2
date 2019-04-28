"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import mainapp.views as mainapp
import authapp.views as authapp
import adminapp.views as adminapp

urlpatterns = [
    url(r'^$', mainapp.main, name='index'),
    url(r'^products/', include('mainapp.urls', namespace='products')),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^admin_custom/', include('adminapp.urls', namespace='admin_custom')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
    url(r'^basket/', include('basketapp.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
