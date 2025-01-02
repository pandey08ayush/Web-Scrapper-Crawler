from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrapper.urls')),  # Delegate to scrapper app
    # path('', include('core.urls')),  # Delegate to a core app
]