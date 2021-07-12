from django.urls import path, include
import views as v

urlpatterns = [
    path('', v.projects),
    path('<int:pk>/', v.project),

    path('<int:pk>/users/', v.users),
    path('<int:pk>/users/<int:pk>/', v.del_user),

    path('<int:pk>/issues/', v.issues),
    path('<int:pk>/issues/<int:pk>/', v.issue),

    path('<int:pk>/issues/<int:pk>/comments/', v.comments),
    path('<int:pk>/issues/<int:pk>/comments/<int:pk>/', v.comment),
]
