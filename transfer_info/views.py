from django.shortcuts import render
from django.http import HttpResponse

from .models import Employees

from .database import Database

# Create your views here.

def index(request):
    Database.populatedb()

    try:
        member_list = Employees.objects.all()
    except Employees.DoesNotExist:
         raise Http404("Nothing in the database")
         return
    context = {
        'member_list': member_list,
    }
    return render(request, 'C:\\Users\\DELL\\Desktop\\FT\\transfer_info\\templates\\transfer-info\\index.html', context)
