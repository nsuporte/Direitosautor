from django.shortcuts import render
from .models import Obra
# Create your views here.
def index(request):
    obras = Obra.objects.all
    return render(request,'index.html',{'obras':obras})

