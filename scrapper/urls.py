from django.urls import path
from . import views

urlpatterns = [
    path('run-scraper/', views.run_scraper, name="run_scraper"),
    path('',views.index,name='index')
]
