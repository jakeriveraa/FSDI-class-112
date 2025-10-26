from django.urls import path
from .views import HomePageView, AboutPageView, GalleryPageView, MountainPageView, RecipesPageView, TravelPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('gallery/', GalleryPageView.as_view(), name="gallery"),
    path('mountain/', MountainPageView.as_view(), name="mountain"),
    path('recipes/', RecipesPageView.as_view(), name="recipes"),
    path('travel/', TravelPageView.as_view(), name="travel"),
    
]