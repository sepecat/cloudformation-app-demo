from django.urls import path

from . import views


app_name = 'travel'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:countryrestriction_id>/', views.detail, name='detail'),
]
