from django.urls import path
from .views import EventList, EventDetailView, TicketListView, TicketTypesListView, TicketScanView, EventTypeOptionsListView, VisibilityOptionsListView

urlpatterns = [
    path('', EventList.as_view(), name='event-list'), 
    path('<int:event_id>/', EventDetailView.as_view(), name='post-detail-update-delete'),
    path('<int:event_id>/tickets-available/', TicketTypesListView.as_view(), name='tickets-Types'), 
    path('tickets/', TicketListView.as_view(), name='ticket'), 
    path('tickets/scan/', TicketScanView.as_view(), name='ticket-scan'),
    path('types', EventTypeOptionsListView.as_view(), name='event-type-options'),
    path('visibility-options', VisibilityOptionsListView.as_view(), name='visibility-options')
]
