from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    price = models.FloatField()
    creation_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField()
    is_sports = models.BooleanField(default=False)

    participants = models.ManyToManyField('users.Member', blank=True, related_name='event_participants')
    managers = models.ManyToManyField('users.Member', blank=True, related_name='event_managers')

    def display_managers(self):
        return ', '.join(list(self.managers.all().values_list('user__username', flat=True)))
    
    @property
    def image_url(self):
        return self.image.url if self.image else None

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"<Event: {self.name}>"

