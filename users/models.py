from django.db import models
from django.contrib.auth.models import User


# Create your models here.
SPORTS = [
    ('Cricket', 'Cricket'),
    ('Football', 'Football'),
    ('Tennis', 'Tennis'),
    ('Badminton', 'Badminton'),
    ('Volleyball', 'Volleyball'),
    ('Hockey', 'Hockey'),
    ('Basketball', 'Basketball'),
    ('Table Tennis', 'Table Tennis'),
]

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cms_id = models.CharField(max_length=10)

    sport = models.CharField(choices=SPORTS, max_length=50, null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def __repr__(self) -> str:
        return f"<Member: {self.user.username}>"


class Society(models.Model):
    name = models.CharField(max_length=255)
    president = models.CharField(max_length=100)
    vice_president = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"<Society: {self.name}>"