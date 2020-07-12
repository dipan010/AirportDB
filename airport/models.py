from django.db import models

# Create your models here.
class Airport(models.Model):  
    apid = models.CharField(max_length=20)  
    apname = models.CharField(max_length=100) 
    apcity = models.CharField(max_length=100)  
    apcountry = models.CharField(max_length=100)  
    apIATA = models.CharField(max_length=100)   
    apICAO = models.CharField(max_length=100)  
    aptimezone = models.TimeField(max_length=100)  
    aptype = models.CharField(max_length=100)  
    class Meta:  
        db_table = "airport" 
        
class Airline(models.Model):
    alid = models.CharField(max_length=20)  
    alname = models.CharField(max_length=100) 
    apcountry = models.CharField(max_length=100)  
    apIATA = models.CharField(max_length=100)   
    apICAO = models.CharField(max_length=100)  
    apstate = models.CharField(max_length=100)  
    ap_nooflights = models.CharField(max_length=100)  
    class Meta:
        db_table = "airline"
class Document(models.Model):
    aadharCard_no = models.CharField(max_length=20)  
    passport_no = models.CharField(max_length=100) 
    ticket_no = models.CharField(max_length=100)  
    class Meta:
        db_table = "document"
class Domestic(models.Model):
    did = models.CharField(max_length=20)  
    alname = models.CharField(max_length=100) 
    from_ap = models.CharField(max_length=100)  
    to_ap = models.CharField(max_length=100)   
    no_of_flights = models.CharField(max_length=100)  
    price = models.CharField(max_length=100)  
    flight_time = models.CharField(max_length=100)  
    class Meta:
        db_table = "domestic"
class International(models.Model):
    iid = models.CharField(max_length=20)  
    alname = models.CharField(max_length=100) 
    from_ap = models.CharField(max_length=100)  
    to_ap = models.CharField(max_length=100)   
    no_of_flights = models.CharField(max_length=100)  
    price = models.CharField(max_length=100)  
    flight_time = models.CharField(max_length=100)  
    class Meta:
        db_table = "international"
class Employee(models.Model):
    eid = models.CharField(max_length=20)  
    Name = models.CharField(max_length=100) 
    post = models.CharField(max_length=100)  
    aadharCard_no = models.CharField(max_length=20)  
    passport_no = models.CharField(max_length=100) 
    al_name = models.CharField(max_length=100)  
    class Meta:
        db_table = "employee"
class Flight(models.Model):
    from_ap = models.CharField(max_length=100)
    from_ap_id = models.CharField(max_length=100)    
    to_ap = models.CharField(max_length=100)
    to_ap_id = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)      
    departs = models.CharField(max_length=100)  
    arrival = models.CharField(max_length=100)  
    price = models.CharField(max_length=100)  
    al_name =  models.CharField(max_length=100)  
    class Meta:
        db_table = "flight"
class Passenger(models.Model):
    pid = models.CharField(max_length=20)  
    Name = models.CharField(max_length=100) 
    Nationality = models.CharField(max_length=100)  
    no_of_luggages = models.CharField(max_length=100)  
    class Meta:
        db_table = "passenger"
class Ticket(models.Model):
    
    from_ap = models.CharField(max_length=100)
    from_ap_id = models.CharField(max_length=100)    
    to_ap = models.CharField(max_length=100)
    to_ap_id = models.CharField(max_length=100)
    departs = models.CharField(max_length=100)  
    arrival = models.CharField(max_length=100)  
    class Meta:
        db_table = "ticket"
class Checkin(models.Model):
    passport_no = models.CharField(max_length=100)
    tno = models.CharField(max_length=100)
    class Meta:
        db_table = "Checkin"
class checkflight(models.Model):
    Trip = models.CharField(max_length=20)
    flying_from = models.CharField(max_length=50)
    flying_to = models.CharField(max_length=50)
    adults = models.IntegerField
    child = models.IntegerField
    departs = models.DateField
    returns = models.DateField
    travel_class = models.CharField(max_length=50)
    class Meta:
        db_table = "check"
    