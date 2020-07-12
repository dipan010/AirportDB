from django import forms  
from airport.models import Airport
from airport.models import Airline 
from airport.models import Ticket
from airport.models import Flight
from airport.models import Passenger
from airport.models import checkflight 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class AirportForm(forms.ModelForm):  
    class Meta:  
        model = Airport  
        fields = "__all__"  
class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = "__all__"
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__" 
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"
class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = "__all__"
class CheckflForm(forms.ModelForm):
    class Meta:
        model = checkflight
        fields = "__all__"