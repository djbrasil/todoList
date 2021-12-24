from django.db import models
from django.urls.base import reverse

class SocialNetwork(models.TextChoices):
    YOUTUBE = 'YOUTUBE', 'youtube' 
    WHATSAPP = 'WHATSAPP', 'whatsapp' 
    FACEBOOK = 'FACEBOOK', 'facebook' 
    INSTAGRAM = 'INSTAGRAM', 'instagram' 
    TWITTER = 'TWITTER', 'twitter' 
    PINTEREST = 'PINTEREST', 'pinterest' 
    SNAPCHAT = 'SNAPCHAT', 'snapchat' 
    TIKTOK = 'TIKTOK', 'tiktok' 
    DISCORD = 'DISCORD', 'discord' 
    GITHUB = 'GITHUB', 'Github'  

class TodoListItem(models.Model):
    category = models.CharField(max_length=10, choices=SocialNetwork.choices, blank=True, null=True) 
    link = models.URLField(max_length=300)

    def __str__(self):
        return self.link  