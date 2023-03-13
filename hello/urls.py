from django.urls import path
from .views import HomePageView, AboutPageView, PostPageView # new

urlpatterns = [
     path("about/", AboutPageView.as_view(), name="about"), # new
     path("", HomePageView.as_view(), name="home"),
     path("post/", PostPageView.as_view(), name="post"),
]