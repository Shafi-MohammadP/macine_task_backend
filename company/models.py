from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()


class HappyClientAchievement(models.Model):
    company = models.ForeignKey(
        'Company', related_name='happy_clients', on_delete=models.CASCADE)
    number = models.IntegerField()


class AwardWonAchievement(models.Model):
    company = models.ForeignKey(
        'Company', related_name='awards_won', on_delete=models.CASCADE)
    number = models.IntegerField()


class ProjectAchievement(models.Model):
    company = models.ForeignKey(
        'Company', related_name='projects_completed', on_delete=models.CASCADE)
    number = models.IntegerField()


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(
        upload_to='company_logos/', null=True, blank=True)
    cover_image = models.ImageField(
        upload_to='cover_images/', null=True, blank=True)
    tagline = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    City = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    vision = models.TextField()
    mission = models.TextField()
    recognition = models.TextField()
    momentum = models.TextField()
    compliment = models.TextField()
    social_media = models.ManyToManyField(SocialMedia)


class WorkCompletedImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work_completed_images/')
