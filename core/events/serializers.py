from rest_framework import serializers
from .models import Events, Ticket, TicketType, EventTypeOptions, VisibiltyOptions

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 1 # nuevo

class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

    '''
    {
      "title": "Feria de regalos",
      "date": "2023-09-18",
      "hour": "15:30:00",
      "location": "Lugar del evento",
      "description": "Descripción del nuevo evento",
      "organizers": 1  
    }
    '''

class TicketsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'
        depth = 1


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        #fields = ('ticket_type', 'assigned_to', 'code')
        depth = 1 

class EventTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTypeOptions
        fields = '__all__'

class VisibiltyOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisibiltyOptions
        fields = '__all__'