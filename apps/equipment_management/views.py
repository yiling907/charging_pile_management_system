from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Equipment
def index(request):
    newest_eq = Equipment.objects.order_by('-create_date')[:15]
    context = {'newest_eq': newest_eq}
    return render(request, 'index.html', context)