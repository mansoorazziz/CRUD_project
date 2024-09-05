from django.http import HttpResponse
from django.template import loader
from members.models import Member
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='% login %')
def members(request):
  #if 'session_name' in request.session:
   # del request.session['session_name']
    # return render(request,'main.html')

  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }

  return HttpResponse(template.render(context, request))
  #else:
   # main(request)
    #return render(request,'main.html')


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  #request.session['session_name'] = 'allowed'
  return render(request,'main.html')
  # template = loader.get_template('main.html')
  # return HttpResponse(template.render(request))

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def c_form(request):
  return render(request,'contact.html')


def save_item(request):
  if request.method=="POST":
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    cell_num = request.POST.get('fone')
    datee = request.POST.get('jday')
    en=Member(firstname = first_name , lastname = last_name , phone = cell_num , joined_date = datee)
    en.save()
    n = 'Saved'
  return render(request,'contact.html', {'n' :n})

def new_form(request):
  return render (request,'contact_form.html')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})

def sign_in(request):
  return render (request,'main.html')

def sign_out(request):
  return render (request,'main.html')