from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import FootballerForm

# Create your views here.
from .models import Footballer


def homePage(request):
    return render(request, "homepage.html")



def addFootballer(request):
    form = FootballerForm(request.POST or None)

    if form.is_valid():
        currentFootballer = form.save(commit=False)
        currentFootballer.save()
        messages.success(request, "Futbolcu başarıyla kaydedildi...")
        return redirect("footballerdashboard")

    context = {"form": form}
    return render(request, "addfootballer.html", context=context)


def footballerDashboard(request):
    footballers = Footballer.objects.filter()
    print(footballers[0].team)
    context = {"footballers": footballers}
    return render(request, "footballerdashboard.html", context=context)


def updateFootballer(request, id):
    footballer = get_object_or_404(Footballer, id=id)
    form = FootballerForm(request.POST or None, instance=footballer)

    if form.is_valid():
        currentFootballer = form.save(commit=False)
        currentFootballer.save()
        messages.success(request, "Futbolcu başarıyla güncellendi...")
        return redirect("footballerdashboard")

    context = {"form": form}
    return render(request, "updatefootballer.html", context=context)


def deleteFootballer(request, id):
    footballer = get_object_or_404(Footballer, id=id)
    footballer.delete()
    messages.success(request, "Futbolcu sistemden başarıyla silindi.")
    return redirect("footballerdashboard")  # article/dashboard