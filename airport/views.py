from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm
from airport.forms import CreateUserForm
from airport.forms import AirportForm  
from airport.models import Airport
from airport.models import Airline
from airport.forms import AirlineForm
from airport.forms import TicketForm  
from airport.models import Ticket
from airport.models import Flight
from airport.forms import FlightForm
from airport.forms import PassengerForm
from airport.models import Passenger 
# Create your views here.
def CSIAPage(request):
    context = {}
    return render(request,'CSIA.html',context)  
def IGIAPage(request):
    context = {}
    return render(request,'IGIA.html',context)  
def KIAPage(request):
    context = {}
    return render(request,'KIA.html',context)  
def HIAPage(request):
    context = {}
    return render(request,'HIA.html',context)  
def FIAPage(request):
    context = {}
    return render(request,'FIA.html',context)  
def DIAPage(request):
    context = {}
    return render(request,'DIA.html',context)  
def DBIAPage(request):
    context = {}
    return render(request,'DBIA.html',context)  
def LAIAPage(request):
    context = {}
    return render(request,'LAIA.html',context)  

def dashboard(request):
    context = {}
    return render(request,'dashboard.html',context)
def aboutPage(request):
    context = {}
    return render(request,'about.html',context)
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)
def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
    context = {}
    return render(request,'login.html',context)
def ap(request):  
    if request.method == "POST":  
        form = AirportForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = AirportForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    airports = Airport.objects.all()  
    return render(request,"show.html",{'airports':airports})  
def edit(request, id):  
    airport = Airport.objects.get(id=id)  
    return render(request,'edit.html', {'airport':airport})  
def update(request, id):  
    airport = Airport.objects.get(id=id)  
    form = AirportForm(request.POST, instance = airport)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'airport': airport})  
def destroy(request, id):  
    airport = Airport.objects.get(id=id)  
    airport.delete()  
    return redirect("/show")  
def al(request):  
    if request.method == "POST":  
        form = AirlineForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_al')  
            except:  
                pass  
    else:  
        form = AirlineForm()  
    return render(request,'index_al.html',{'form':form})  
def show_al(request):  
    airlines = Airline.objects.all()  
    return render(request,"show_al.html",{'airlines':airlines})  
def edit_al(request, id):  
    airline = Airline.objects.get(id=id)  
    return render(request,'edit_al.html', {'airline':airline})  
def update_al(request, id):  
    airline = Airline.objects.get(id=id)  
    form = AirlineForm(request.POST, instance = airline)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_al")  
    return render(request, 'edit_al.html', {'airline': airline})  
def destroy_al(request, id):  
    airline = Airline.objects.get(id=id)  
    airline.remove()  
    return redirect("/show_al")  
def tk(request):  
    if request.method == "POST":  
        form = TicketForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_tk')  
            except:  
                pass  
    else:  
        form = TicketForm()  
    return render(request,'index_tk.html',{'form':form})  
def show_tk(request):  
    tickets = Ticket.objects.all()  
    return render(request,"show_tk.html",{'tickets':tickets})  
def edit_tk(request, id):  
    ticket = Ticket.objects.get(id=id)  
    return render(request,'edit_tk.html', {'ticket':ticket})  
def update_tk(request, id):  
    ticket = Ticket.objects.get(id=id)  
    form = TicketForm(request.POST, instance = ticket)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_tk")  
    return render(request, 'edit_tk.html', {'ticket': ticket})  

def fl(request):  
    if request.method == "POST":  
        form = FlightForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_fl')  
            except:  
                pass  
    else:  
        form = FlightForm()  
    return render(request,'index_fl.html',{'form':form})  
def show_fl(request):  
    flights = Flight.objects.all()  
    return render(request,"show_fl.html",{'flights':flights})  
def ps(request):  
    if request.method == "POST":  
        form = PassengerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_ps')  
            except:  
                pass  
    else:  
        form = FlightForm()  
    return render(request,'index_ps.html',{'form':form})  
def show_ps(request):  
    passengers = Passenger.objects.all()  
    return render(request,"show_ps.html",{'passengers':passengers})  
