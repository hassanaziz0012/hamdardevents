from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cms_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    
    def __repr__(self) -> str:
        return f"<Member: {self.user.username}>"
