from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('innerpage', views.index, name = 'innerpage' ),
    path('portfoliodetails', views.index, name = 'portfoliodetails' )
]