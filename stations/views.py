from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


stations_list = []

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Street', 'District']
    reader = csv.DictReader(csvfile)
    for row in reader:
        stations_list.append(row)


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)


    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
