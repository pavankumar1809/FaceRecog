from django.db import models
from django.db.models.signals import post_save

def from_1001():
    largest = UserProfile.objects.all().order_by('face_id').last()
    if not largest:
        return 1001
    return largest.face_id +1

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True,default=from_10001)
    name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length = 20,unique=True)
    def __str__(self):
        return self.name