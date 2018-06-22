from utils.unique_id import PushID

from django.db import models
from django.contrib.auth.models import User


class Rides(models.Model):
    ride_id = models.CharField(
        max_length=255, primary_key=True,
        blank=True, null=False, editable=False)
    pick_up = models.TextField(max_length=255, )
    take_off_time = models.DateTimeField()
    destination = models.TextField()
    rider = models.ForeignKey(
        User, related_name='rides',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.ride_id)

    def save(self, *args, **kwargs):
        if len(self.ride_id.strip(" ")) == 0:
            self.ride_id = PushID().next_id()

        super(Rides, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-ride_id']
