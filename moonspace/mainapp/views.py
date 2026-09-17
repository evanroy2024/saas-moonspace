from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import MoonPlot

def home(request):
    return render(request, "index.html")


def buy_gift(request):
    if request.method == "POST":
        
        plot = MoonPlot.objects.create(
            buyer_name=request.POST.get("buyer_name"),
            receiver_name=request.POST.get("receiver_name", ""),
            image=request.FILES.get("image"),
            message=request.POST.get("message", ""),
            song=request.POST.get("song"),
            design=request.POST.get("design", 1),
            wants_reply=request.POST.get("wants_reply") == "on",
            email=request.POST.get("email", ""),
        )

        return redirect("confirmation", url=plot.url)
    
    return render(request, "plots/form.html", {
        "songs": range(1, 21),
        "designs": range(1, 6),
    })

from django.shortcuts import render, get_object_or_404
from .models import MoonPlot


def confirmation(request, url):
    plot = get_object_or_404(MoonPlot, url=url)

    return render(request, "users/confirmation.html", {
        "plot": plot
    })

from django.shortcuts import render, get_object_or_404
from .models import MoonPlot


def moon_plot(request, url):

    plot = get_object_or_404(MoonPlot, url=url)

    return render(request, f"users/design{plot.design}.html", {
        "plot": plot
    })

# FOR PUBLIC VIEW -------------------------------------------------------------
def all_plots(request):
    plots = MoonPlot.objects.all()

    return render(request, "plots/2d_plots.html", {
        "plots": plots
    })


def plot_view(request):
    plots = MoonPlot.objects.all()

    return render(request, "plots/plots.html", {
        "plots": plots
    })

def plot_2d(request):
    plots = MoonPlot.objects.all()

    return render(request, "plots/2d_plots.html", {
        "plots": plots
    })

def plot_3d(request):
    plots = MoonPlot.objects.all()

    return render(request, "plots/3d_plots.html", {
        "plots": plots
    })



# SPECIFIC PLOTS FIND -------------------------------------------------------------
def specific_plot(request, url):
    plot = get_object_or_404(MoonPlot, url=url)

    # pull only up to 29 others, so even with thousands of rows we never load more than 30 total
    other_plots = MoonPlot.objects.exclude(pk=plot.pk).order_by('-id')[:29]
    plots = [plot] + list(other_plots)

    return render(request, "specific/specific_plot.html", {
        "plot": plot,
        "plots": plots,
    })

def specific_moon_plot(request, url):
    plot = get_object_or_404(MoonPlot, url=url)

    # pull only up to 29 others, so even with thousands of rows we never load more than 30 total
    other_plots = MoonPlot.objects.exclude(pk=plot.pk).order_by('-id')[:29]
    plots = [plot] + list(other_plots)

    return render(request, "specific/plot_moon.html", {
        "plot": plot,
        "plots": plots,
    })









# THemes --------------------------------------------------------------
def theme1(request):
    return redirect("/03abf802/")


def theme2(request):
    return redirect("/03abf802/")


def theme3(request):
    return redirect("/03abf802/")


def theme4(request):
    return redirect("/03abf802/")


def theme5(request):
    return redirect("/03abf802/")