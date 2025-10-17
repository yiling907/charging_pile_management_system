"""charging_pile_management_system URL Configuration

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
from django.urls import path
from drf_yasg import openapi #new foe swagger
from drf_yasg.views import get_schema_view as swagger_get_schema_view #new foe swagger
from django.urls import path, include

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="charging pile management system APIs",
        default_version='1.0.0',
        description="charging pile management system swagger",
    ),
    public=True,
)

urlpatterns = [
    path("", include('apps.equipment_management.urls')),
    path("admin/", admin.site.urls),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),

]
