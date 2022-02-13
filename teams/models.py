from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=100)
    blurb = models.CharField(max_length=280)
    hero_image = models.ImageField(upload_to='team_image/', blank=True)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='teams')
    custom_prompt = models.CharField(max_length=150)
    collab_prompt = models.CharField(max_length=150)
    required_fields = models.CharField(max_length=100)
    link = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='members')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True)
    goes_by = models.CharField(max_length=25, blank=True)
    pronouns = models.CharField(max_length=25, blank=True)
    avatar = models.ImageField(upload_to='user_image/', blank=True)
    link = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    loc_lat = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    loc_long = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    interests = models.CharField(max_length=280, blank=True)
    pets = models.CharField(max_length=100, blank=True)
    custom_answer = models.CharField(max_length=280, blank=True)
    collab_answer = models.CharField(max_length=280, blank=True)
    reactions_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
