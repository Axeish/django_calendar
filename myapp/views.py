# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Entry

# Create your views here.


def index(request):
    entries = Entry.objects.all()
    endict = {'entries':entries}
    return render(request, 'myapp/index.html', endict)

def details(request,pk):
    entry = Entry.objects.get(id=pk)
    return render(request, "myapp/details.html",{'entry':entry})    
