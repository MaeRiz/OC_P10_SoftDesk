from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_projects import views as p_views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('signup/'),
    path('login/'),

    path('projects/', include('app_projects.urls')),

]
