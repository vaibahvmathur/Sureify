from django.shortcuts import render
from models import Footballers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.views.decorators.csrf import csrf_exempt


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name + '.png' in files:
            return 1


@csrf_exempt
def HomePage(request):
    select = '0'
    players_list = {}
    if request.GET:
        if request.GET.get('skills'):
            skills = str(request.GET.get('skills'))
            select = skills
            if request.GET.get('player_name'):
                name = str(request.GET.get('player_name'))
                players_list = Footballers.objects.filter(skill_moves=skills, name__icontains=name)
            else:
                players_list = Footballers.objects.filter(skill_moves=skills)
        elif request.GET.get('player_name'):
            name = str(request.GET.get('player_name'))
            players_list = Footballers.objects.filter(name__icontains=name)
        else:
            players_list = Footballers.objects.all()
    elif not len(players_list):
        players_list = Footballers.objects.all()
    else:
        players_list = Footballers.objects.all()
    for player in players_list:
        if find(player.name, 'football/static/football/img/pictures'):
            temp = str('football/img/pictures/' + player.name + '.png')
            if not player.player_img:
                player.player_img = temp
                player.save()
    paginator = Paginator(players_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        players_details = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        players_details = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        players_details = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'players_details': players_details, 'select': select})
