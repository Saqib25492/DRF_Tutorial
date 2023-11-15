from django.urls import path
from search import views


urlpatterns = [
    path('', views.SearchListView.as_view(), name='search'),
    path('searchold/', views.SeacrholdListView.as_view(), name='searchold')
]
