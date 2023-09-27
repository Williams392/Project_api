import uuid
from django.db import models
from fundamentals.models import Club
from authentication.models import Profile
from fundamentals.models import Currency
from django.core.validators import MinValueValidator

class VisibiltyOptions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class StatusOptions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class EventTypeOptions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Events(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    visibility = models.ForeignKey(VisibiltyOptions, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(StatusOptions, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    hour = models.TimeField(null=False, blank=False)
    location = models.CharField(max_length=350, null=False, blank=False)
    e_type = models.ForeignKey(EventTypeOptions, on_delete=models.PROTECT, null=True, blank=True) 
    description = models.TextField(null=False, blank=False)
    event_banner = models.ImageField(upload_to='event_banners/', null=True, blank=True)

    organizers = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.title
    
# Asistentes: 
class Presents(models.Model):
    id_profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey(Events, on_delete=models.PROTECT, null= False)  
    attending = models.BooleanField(default=False)  # (asistiendo) confirmación de si el usuario asistio al evento.
    
    def __str__(self):
        return self.id_profile 
    
# Interesados:
class Interested(models.Model):
    id_profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey (Events, on_delete=models.PROTECT, null= False)

    def __str__(self): # Nombre del Perfil - Título del Evento
        return f"{self.profile} - {self.event}"
    
    
class TicketType(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, blank=True)
    max_number_to_issue = models.PositiveIntegerField(validators=[MinValueValidator(1)] ,null=True, blank=True)
    remaining_tickets = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True, blank=True)

    def __str__(self):
        return f"{self.event} - {self.name}"

class Ticket(models.Model):
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Profile, on_delete=models.PROTECT)
    code = models.UUIDField(default = uuid.uuid4, editable = False)
    scan_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ticket_type} - {self.assigned_to}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Si se está creando un nuevo objeto
            print(self.ticket_type.remaining_tickets)
            self.ticket_type.remaining_tickets = self.ticket_type.remaining_tickets - 1 # Generar una clave aleatoria
            self.ticket_type.save()
        super().save(*args, **kwargs)