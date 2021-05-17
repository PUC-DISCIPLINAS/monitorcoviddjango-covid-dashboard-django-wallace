from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.context_processors import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic import ListView, View
from .forms import CovidForm
# Create your views here.
from .models import (DataInfo, Country)


@login_required(login_url='/login/')
def home_page(request):
    template_name = 'index.html'
    # dictionary for initial data with
    # field names as keys
    context = {}

    context['datainfos'] = DataInfo.objects.all()
    context['countrys'] = Country.objects.all()
    return render(request, template_name, context)

def painel_page(request):
    template_name = 'painel.html'
    # dictionary for initial data with
    # field names as keys
    context = {}

    context['datainfos'] = DataInfo.objects.all()
    context['countrys'] = Country.objects.all()
    return render(request, template_name, context)

class Create(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Create, self).dispatch(*args, **kwargs)

    def get(self, request):
        # adiciooar um verificador no country que  pega o id apartir de um nome
        country_data = request.GET.get('country', None)
        country, create = Country.objects.get_or_create(name=country_data)
        country_serializer = serializers.serialize('json', [country, ])

        confirmed_cases_data = request.GET.get('confirmedCases', None)
        deaths_data = request.GET.get('deaths', None)
        recovered_data = request.GET.get('recovered', None)

        DataInfo.objects.update_or_create(
            country=country,
            defaults={
                'confirmedCases': confirmed_cases_data,
                'deaths': deaths_data,
                'recovered': recovered_data
            }
        )

        obj = DataInfo.objects.get(country__name=country.name)

        data = {'id': obj.id, 'country': country.name, 'confirmedCases': obj.confirmedCases, 'deaths': obj.deaths,
                'recovered': obj.recovered}

        data = {
            'datainfo': data
        }
        return JsonResponse(data)


class UpdateView(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

    def get(self, request):
        country_data = request.GET.get('country', None)
        confirmed_cases_data = request.GET.get('confirmedCases', None)
        deaths_data = request.GET.get('deaths', None)
        recovered_data = request.GET.get('recovered', None)

        obj = DataInfo.objects.get(country=country_data)
        obj.country = country_data
        obj.confirmedCases = confirmed_cases_data
        obj.deaths = deaths_data
        obj.recovered = recovered_data

        obj.save()

        data = {'id': obj.id, 'country': obj.country, 'confirmedCases': obj.confirmedCases, 'deaths': obj.deaths,
                'recovered': obj.recovered}

        data = {
            'datainfo': data
        }
        return JsonResponse(data)


class Find(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Find, self).dispatch(*args, **kwargs)

    def get(self, request):
        country_data = request.GET.get('name', None)
        obj = None
        if country_data is not None:
            try:
                country = Country.objects.get(name=country_data)
                obj = DataInfo.objects.get(country__name=country.name)
                data = {'id': obj.id, 'country': country.name, 'confirmedCases': obj.confirmedCases,
                        'deaths': obj.deaths,
                        'recovered': obj.recovered}

                return JsonResponse(data)

            except ObjectDoesNotExist:
                print("Objeto não encontrado!")
            except ValueError as err:
                print("Objeto: {}".format(err))

        return JsonResponse({"erro":"nãoencontrado"})


# delete view for details
class DeleteView(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

    def get(self, request):
        id1 = request.GET.get('id', None)
        print(id1)
        DataInfo.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def login_page(request):
    template_name = 'login.html'

    return render(request, template_name)


@csrf_protect
def authenticate_login(request):
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            print('encontrou')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Senha ou Usuário incorretos.')
        return redirect('/login')


def logout_user(request):
    logout(request)
    return redirect('/')
