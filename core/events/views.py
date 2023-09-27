from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Events, Ticket, TicketType, EventTypeOptions, VisibiltyOptions
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

from authentication.models import Profile
import uuid

class EventList(APIView):
    def get(self, request, format=None):
        club_id = request.query_params.get('club-id', False)
        if club_id:
            queryset = Events.objects.filter(organizers__rotary_club_id = club_id)
        else:
            queryset = Events.objects.all()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventCreateUpdateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EventDetailView(APIView):
    def get(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id) 
        serializer = EventsSerializer(event)
        return Response(serializer.data)

    def put(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id)
        serializer = EventCreateUpdateSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TicketTypesListView(APIView):
    def get(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id) 
        tickets_available = TicketType.objects.filter(event = event)
        serializer = TicketsTypeSerializer(tickets_available, many=True)
        return Response(serializer.data)

class TicketListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        profile = Profile.objects.get(user = user)
        event_id = request.query_params.get('event-id', False)
        if event_id:
            event = get_object_or_404(Events, pk=event_id) 
            tickets = Ticket.objects.filter(ticket_type__event = event, assigned_to = profile)
        else:
            tickets = Ticket.objects.filter(assigned_to = profile)
        serializer = TicketsSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        profile = Profile.objects.get(user = user)
        ticket_type = request.query_params.get('ticket-type', False)
        if not ticket_type:
            return Response(
                {
                    'message': 'Ticket type is required'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            ticket_type = get_object_or_404(TicketType, pk=ticket_type)
            ticket, created = Ticket.objects.get_or_create(ticket_type = ticket_type, assigned_to = profile)
            serializer = TicketsSerializer(ticket)
            return Response(serializer.data)
        
    
class TicketScanView(APIView):
    
    def post(self, request, format=None):
        code = request.data.get('code', None)
        
        if not code:
            response_data = {
                'message': 'Ticket code is required'
            }
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            try:
                uuid_obj = uuid.UUID(code)
            except ValueError:
                response_data = {
                    'message': 'UUID invalid'
                }
                status_code = status.HTTP_400_BAD_REQUEST
            else:
                try:
                    ticket = Ticket.objects.get(code=code)
                except Ticket.DoesNotExist:
                    response_data = {
                        'message': 'No valid ticket found'
                    }
                    status_code = status.HTTP_404_NOT_FOUND
                else:
                    response_data = {
                        'message': 'Ticket scanned successfully.'
                    }
                    status_code = status.HTTP_202_ACCEPTED
                    ticket.scan_done = True
                    ticket.save()

        return Response(response_data, status=status_code)
    
class EventTypeOptionsListView(APIView):
    def get(self, request, format=None):
        events_types = EventTypeOptions.objects.all()
        serializer = EventTypesSerializer(events_types, many=True)
        return Response(serializer.data)
    
class VisibilityOptionsListView(APIView):
    def get(self, request, format=None):
        visibility_options = VisibiltyOptions.objects.all()
        serializer = VisibiltyOptionsSerializer(visibility_options, many=True)
        return Response(serializer.data)
    