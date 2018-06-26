from utils.unique_id import PushID

from django.db import models
from django.contrib.auth.models import User


class OfferRides(models.Model):
    offer_id = models.CharField(
        max_length=255, primary_key=True,
        blank=True, null=False, editable=False)
    pick_up = models.TextField(max_length=255, )
    take_off_time = models.DateTimeField()
    destination = models.TextField()
    available_space = models.IntegerField(null=True)
    user = models.ForeignKey(
        User, related_name='rides',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.offer_id)

    def save(self, *args, **kwargs):
        if len(self.offer_id.strip(" ")) == 0:
            self.offer_id = PushID().next_id()

        super(OfferRides, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-offer_id']


class RequestRides(models.Model):
    request_id = models.CharField(
        max_length=50, primary_key=True,
        blank=True, null=False, editable=False
    )
    user = models.ForeignKey(
        User, related_name='offer_rides',
        on_delete=models.CASCADE)
    offer = models.ForeignKey(
        OfferRides, related_name='offer_rides',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.request_id)

    def save(self, *args, **kwargs):
        if len(self.request_id.strip(" ")) == 0:
            self.request_id = PushID().next_id()

        super(RequestRides, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-request_id']
