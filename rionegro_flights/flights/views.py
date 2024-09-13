from django.shortcuts import render, redirect
from .models import Flight
from .forms import FlightForm
from django.db.models import Avg

def home(request):
    return render(request, 'home.html')

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
    else:
        form = FlightForm()
    return render(request, 'register_flight.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'list_flights.html', {'flights': flights})

def statistics(request):
    national_count = Flight.objects.filter(type='Nacional').count()
    international_count = Flight.objects.filter(type='Internacional').count()
    average_price_national = Flight.objects.filter(type='Nacional').aggregate(Avg('price'))['price__avg']
    return render(request, 'statistics.html', {
        'national_count': national_count,
        'international_count': international_count,
        'average_price_national': average_price_national
    })
