from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class GalleryPageView(TemplateView):
    template_name = "pages/gallery.html"

class MountainPageView(TemplateView):
    template_name = "pages/mountain.html"

class RecipesPageView(TemplateView):
    template_name = "pages/recipes.html"

class TravelPageView(TemplateView):
    template_name = "pages/travel.html"