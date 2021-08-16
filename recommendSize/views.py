from django.shortcuts import render
from .models import Measurement, SizeGuide, ClothingItem, Store

# Create your views here.
# homepage
def homepage(request):
    return render(request, 'recommendSize/homepage.html')
