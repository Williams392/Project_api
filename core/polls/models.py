from django.db import models
from clubs.models import Member
from fundamentals.models import Club

# Create your models here.
class Survey(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    deadline_date = models.DateField()
    deadline_time = models.TimeField()
    is_open = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Option(models.Model):
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.survey} - {self.option_text}"

class Vote(models.Model):
    # id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='votes', on_delete=models.CASCADE)
    voted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.option}"

