from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import FootballTeamForm
from .models import FootballTeam


def prepareTeams(teams):
    for team in teams:
        footballers = team.footballer_set.all()
        for footballer in footballers:
            team.squad.append(footballer)

    for team in teams:
        team.numOfTeamMembers = len(team.footballer_set.all())
        for footballer in team.footballer_set.all():
            team.teamPower += footballer.overall
            team.squadValue += footballer.marketValue

        print(team)

    return teams


# Create your views here.
def teamDashboard(request):
    teams = FootballTeam.objects.filter()
    teams = prepareTeams(teams)
    context = {"teams": teams}
    return render(request, "teamdashboard.html", context=context)


def addTeam(request):
    form = FootballTeamForm(request.POST or None)

    if form.is_valid():
        currentTeam = form.save(commit=False)
        currentTeam.save()
        messages.success(request, "Takım başarıyla kaydedildi...")
        return redirect("teamdashboard")

    context = {"form": form}
    return render(request, "adddteam.html", context=context)


def updateTeam(request, id):
    team = get_object_or_404(FootballTeam, id=id)
    form = FootballTeamForm(request.POST or None, instance=team)

    if form.is_valid():
        currentTeam = form.save(commit=False)
        currentTeam.save()
        messages.success(request, "Takım başarıyla güncellendi...")
        return redirect("teamdashboard")

    context = {"form": form}
    return render(request, "updateteam.html", context=context)


def deleteTeam(request, id):
    team = get_object_or_404(FootballTeam, id=id)
    team.delete()
    messages.success(request, "Takım sistemden başarıyla silindi.")
    return redirect("teamdashboard")  # article/dashboard


def teamDetail(request, id):
    team = get_object_or_404(FootballTeam, id=id)
    context = {"team": team}
    return render(request, "teamdetail.html", context=context)
