from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

from django.contrib.auth.decorators import login_required

def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM events")
        events = dictfetchall(cursor)
    
    return render(request, 'ase_hw2_site/index.html',{
        'events': events,
    })

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]