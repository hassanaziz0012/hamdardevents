from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    creation_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField()

    participants = models.ManyToManyField('users.Member', blank=True)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"<Event: {self.name}>"
