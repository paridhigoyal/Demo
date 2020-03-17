from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('vehicles/', views.VehicleView.as_view()),
    path('deal',views.DealView.as_view()),
    path('rating',views.RatingView.as_view()),
path('rating/<int:pk>/',views.RatingDetail.as_view())
]