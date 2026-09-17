from django.urls import path
from .views import  buy_gift, confirmation , home, moon_plot ,all_plots , plot_view , plot_2d , plot_3d, specific_moon_plot , specific_plot
from .views import theme1, theme2, theme3, theme4, theme5
urlpatterns = [
    path("", home, name="home"),
    path("buy/", buy_gift, name="buy_gift"),
    path("all/", all_plots, name="all_plots"),
    path("plots/", plot_view, name="plot_view"),
    path("plot/2d/", plot_2d, name="plot_2d"),
    path("plot/3d/", plot_3d, name="plot_3d"),
    path("theme1/", theme1, name="theme1"),
    path("theme2/", theme2, name="theme2"),
    path("theme3/", theme3, name="theme3"),
    path("theme4/", theme4, name="theme4"),
    path("theme5/", theme5, name="theme5"),
    path("<str:url>/", moon_plot, name="moon_plot"),

    # specific plots urls 
    path("your/<str:url>/", specific_plot, name="specific_plot"),
    path("moon/<str:url>/", specific_moon_plot, name="specific_moon_plot"),

    path("confirmation/<str:url>/", confirmation, name="confirmation"),


    
]