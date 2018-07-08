from django.db import models


class OfferRides(models.Model):
    
    """
        Class OfferRides Models
    """
    __tablename__ = 'Offerrides'

    pick_up = models.TextField(max_length=255, )
    take_off_time = models.DateTimeField()
    destination = models.TextField()
    available_space = models.IntegerField()
    owner = models.ForeignKey(
        'auth.User', related_name='offer_rides', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.pick_up, self.id)

    class Meta:
        ordering = ['-id']


class RequestRides(models.Model):
    
    """
        Class RequestRides Models
    """
    __tablename__ = 'RequestRides'

    owner = models.ForeignKey(
        'auth.User', related_name='request_rides',
        on_delete=models.CASCADE)
    offerrides = models.ForeignKey(
        OfferRides, related_name='requestrides',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.owner, self.id)

    class Meta:
        ordering = ['-id']
