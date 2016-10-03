from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages

from .forms import EventsForm

from django.contrib.auth.decorators import login_required

def index(request):    
    #if this is a POST request
    if request.method == 'POST':
        form = EventsForm(request.POST)
        #check for validation
        if form.is_valid():
            #form.save()
            data = form.cleaned_data
            with connection.cursor() as cursors:
                cursors.execute("INSERT INTO events (tag,time,expiration,description, location) VALUES (%s,%s,%s,%s,%s);",
                                [data['tag'],data['time'],data['expiration'],data['description'],data['location']])
            return HttpResponse("Thank you for submiting")
        else:
            HttpResponse("Not successful")
    else:
        form = EventsForm()
            
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM events;")
        events = dictfetchall(cursor)
    eventsform = EventsForm();
    
    
    return render(request, 'ase_hw2_site/index.html',{
        'events': events,
        'events_form': eventsform,
        'form': form,
    })

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]