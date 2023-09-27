from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import Survey, Option, Vote
from .serializers import SurveySerializer, OptionSerializer, VoteSerializer

class SurveyListCreateView(APIView): # (EncuestasList)

    def get_surveys_by_club(self, club_id):
        try:
            return Survey.objects.filter(club = club_id)
        except Survey.DoesNotExist:
            return None

    def get(self, request):
        club_id = request.query_params.get('club-id', None)
        surveys = self.get_surveys_by_club(club_id = club_id)
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetailView(APIView): # (EncuestasDetail)

    def get_object(self, pk):
        return get_object_or_404(Survey, pk=pk)

    def get(self, request, pk):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        survey = self.get_object(pk)
        survey.delete()
        # (Encuesta con ID {pk} eliminad)
        return Response({"msg": f"Survey with ID {pk} deleted"})

    def post(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OptionListCreateView(APIView):

    def get(self, request):
        options = Option.objects.all()
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            survey_id = request.data.get('survey') # encuesta
            survey = get_object_or_404(Survey, pk=survey_id)
            serializer.save(survey=survey)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteCreateView(APIView):

    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            option_id = request.data.get('option')
            option = get_object_or_404(Option, pk=option_id)
            serializer.save(option=option)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)