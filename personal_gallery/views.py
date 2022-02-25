from django.shortcuts import render
import datetime as dt
from  .models import Image


# Create your views here.

def home(request):
    date = dt.date.today()
    return render(request, 'index.html',{"date": date})

def gallery(request):
    my_gallery= Image.get_images()
    print(my_gallery)
    return render(request, 'gallery.html', {'gallery': my_gallery})