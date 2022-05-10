from django.shortcuts import render


#  main page output
def index(request):
    return render(request, 'main/index.html')


def club(request):
    return render(request, 'main/club.html')


def team(request):
    return render(request, 'main/team.html')
