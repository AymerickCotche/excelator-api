"""
URL configuration for excelator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path(r'api/auth/', include('knox.urls')),
    path(r'api/customauth/', include('customauth.urls')),
    path('admin/', admin.site.urls),
    path("api/grandraid/", include("grandraid.urls")),
    path("api/lesbases/", include("lesbases.urls")),
    path("api/referenceabsolue/", include("referenceabsolue.urls")),
    path("api/eleves/", include("eleves.urls")),
    path("api/facturation/", include("facturation.urls")),
]
