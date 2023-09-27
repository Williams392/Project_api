from rest_framework import serializers
from .models import Survey, Option, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Option
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'deadline_date', 'deadline_time', 'options', 'is_open', 'creation_date', 'edit_date')