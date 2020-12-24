from django.contrib import admin
from django.urls import include, path
# from fscohort.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fscohort.urls')),
]
