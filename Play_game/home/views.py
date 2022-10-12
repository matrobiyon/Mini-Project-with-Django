from django.shortcuts import render
from .models import Calendar,Table 
from django.db.models import Q
from django.http import HttpResponseRedirect 

# Create your views here.

def index(response):
    etaj = Table.objects.order_by('etaj').values_list('etaj', flat=True).distinct()
    dictionary = {
        "etaj" : etaj
    }
    return render(response,"home/home.html", dictionary)

def get_etaj(response,etaj):
    hujraho = ""
    if etaj ==1:
        hujraho = Table.objects.filter(hujra__lte=6).order_by('hujra')
    elif etaj ==2:
        hujraho = Table.objects.filter(Q(hujra__gt=6),Q(hujra__lte=12)).order_by('hujra')
    elif etaj ==3:
        hujraho = Table.objects.filter(Q(hujra__gt=12),Q(hujra__lte=18)).order_by('hujra')
    elif etaj ==4:
        hujraho = Table.objects.filter(Q(hujra__gt=18),Q(hujra__lte=24)).order_by('hujra')
    elif etaj ==5:
        hujraho = Table.objects.filter(Q(hujra__gt=24),Q(hujra__lte=30)).order_by('hujra')
    elif etaj ==6:
        hujraho = Table.objects.filter(Q(hujra__gt=30),Q(hujra__lte=36)).order_by('hujra')
    elif etaj ==7:
        hujraho = Table.objects.filter(Q(hujra__gt=36),Q(hujra__lte=42)).order_by('hujra')
    elif etaj ==8:
        hujraho = Table.objects.filter(Q(hujra__gt=42),Q(hujra__lte=48)).order_by('hujra')
    elif etaj ==9:
        hujraho = Table.objects.filter(Q(hujra__gt=48),Q(hujra__lte=54)).order_by('hujra')
    elif etaj ==10:
        hujraho = Table.objects.filter(Q(hujra__gt=54),Q(hujra__lte=60)).order_by('hujra')
    elif etaj ==11:
        hujraho = Table.objects.filter(Q(hujra__gt=60),Q(hujra__lte=66)).order_by('hujra')
    elif etaj ==12:
        hujraho = Table.objects.filter(Q(hujra__gt=66),Q(hujra__lte=72)).order_by('hujra')
    dictionary = {
        "hujraho":hujraho,
        "etaj":etaj
    }
    return render(response, "home/etaj.html", dictionary)

def malumot(response, etaj,hujra):
    malumot = Calendar.objects.filter(spisok_id=hujra).order_by('date')
    spisok = Table.objects.get(id=hujra)
    dictionary = {
        "malumot":malumot,
        "spisok":spisok
    }
    return render(response,'home/malumot.html',dictionary)
