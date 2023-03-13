from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post


class PostPageView(ListView):
    model = Post
    template_name = "post.html"


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView): # new
    template_name = "about.html"
