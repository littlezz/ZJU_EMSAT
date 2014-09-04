from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, CreateNicknameForm
from .models import get_or_create_user
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .thread_test import something
import json
from .models import CourseDetail
from django.http import JsonResponse
from .lib import choose
# Create your views here.


def welcome(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            schoolid = form.cleaned_data['schoolid']
            password = form.cleaned_data['password']


            created = get_or_create_user(username=schoolid, password=password)
            user = authenticate(username=schoolid,password=password)
            if user:
                login(request,user)
            if created:
                return HttpResponseRedirect(reverse('create_nickname'))
            else:
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()

    return render(request, 'welcome.html', {'form':form})

@login_required
def create_nickname(request):
    if request.method =='POST':
        form = CreateNicknameForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            user = request.user
            user.first_name = nickname
            user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CreateNicknameForm()

    return render(request, 'create_nickname.html', {'form':form})

@login_required
def home(requets):
    ipadress = requets.META['REMOTE_ADDR']



    return render(requets,'home.html')


def out(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))

def test_ajax(requests):
    t=choose.Table()
    t.user_fullcourse()
    vdict = t.table
    #response = HttpResponse(json.dumps(vdict), content_type='application/json')
    #response.status = 200

    response = JsonResponse(vdict)
    return  response