from django.http import HttpResponse
from django.template import loader
from members.models import Member
from django.shortcuts import render

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

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