# from audioop import reverse
from django.urls import reverse
from re import template
from django.shortcuts import render
from .models import Members
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def index(request):
    template= loader.get_template("index.html")
    mymembers=Members.objects.all().values()
    # output= " "
    # for x in mymembers:
    #     output += x['firstname'] + x['lastname']
    context={
        'mymembers': mymembers
    }    
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x= request.POST['first']
    y=request.POST['last']
    member=Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member=Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
    mymember=Members.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    first= request.POST['first']
    last= request.POST['last']
    member= Members.objects.get(id=id)
    member.firstname= first
    member.lastname= last
    member.save()
    return HttpResponseRedirect(reverse('index'))




    

