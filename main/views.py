from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import json
import string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


with open('main/country.json', 'r') as f:
    text=json.load(f)


def get_country(request,country):
    with open('main/country.json', 'r') as f:
        data=json.load(f)
    for i in range(0, len(data)):
        context={
            'country':data[i]['country'],
            'language':data[i]['languages']
        }

        def get_key(d,value):
            for k,v in d.items():
                if v==value:
                    return k
        info=get_key(data[i], country)
        if info:
            return render(request, 'main/language.html',context=context)
        else:
            continue
    return HttpResponseNotFound('Данной страны не существует')


def get_language(request,languages):
    with open('main/country.json', 'r') as f:
        data=json.load(f)
    list_countries = []
    for i in range(0, len(data)):
        if languages in data[i]['languages']:
            list_countries.append(data[i]['country'])
    for i in range(0, len(data)):
        context = {
            "data": data[i],
            'country': data[i]['country'],
            'language': data[i]['languages'],
            'lang_main': languages,
            'countrys': list_countries
        }
        if languages in data[i]['languages']:
            return render(request, 'main/countries.html', context=context)
        else:
            continue
    return HttpResponseNotFound('Данной страны не существует')


def get_letter(request, letter):
    with open('main/country.json', 'r') as fi:
        data = json.load(fi)
    list_c = []
    dick = {}
    alf = []
    for i in range(0, len(data)):
        if data[i]['country'][0] not in alf:
            alf.append(data[i]['country'][0])
        uurl = reverse('con', args=[data[i]['country']])
        if data[i]['country'][0] == str(letter):
            list_c.append(data[i]['country'])
        dick[data[i]['country']] = uurl
    alf.sort()
    object_list = list_c
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 6)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    if list_c:
        context = {
            'alf': alf,
            's': list(string.ascii_uppercase),
            'letter': list_c,
            'page_obj': page_obj,
        }
        return render(request, 'main/countries_list.html', context=context)
    return HttpResponse('Данной страны не существует')


def get_data(request):
    with open('main/country.json', 'r') as fi:
        data=json.load(fi)
    uurl_l = []
    dick={}
    alf = []
    for i in range(0, len(data)):
        if data[i]['country'][0] not in alf:
            alf.append(data[i]['country'][0])
    for i in range(0,len(data)):
        uurl= reverse('con',args=[data[i]['country']])
        uurl_l.append(uurl)
        dick[data[i]['country']]=uurl
    alf.sort()

    object_list=[]
    for i in text:
        object_list.append((i['country']))
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 6)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context={
        'dick':dick,
        'page_obj':page_obj,
        'alf':alf,
        's':list(string.ascii_uppercase)
    }
    return render(request,'main/countries_list.html',context=context)


def get_data2(request):
    with open('main/country.json', 'r') as fi:
        data=json.load(fi)
    list_lan = []
    for i in range(0,len(data)):
        for j in data[i]['languages']:
            if j not in list_lan:
                list_lan.append(j)
    list_lan.sort()

    context={
        'list':list_lan,
    }
    return render(request,'main/languages_list.html',context=context)


def index(request):
    return render(request, 'main/index.html')
