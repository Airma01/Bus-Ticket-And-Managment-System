from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SelamBusInfo(models.Model):
    bus_name =models.CharField(max_length=200,default='selam_bus')
    starting_point = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance_by_km=models.BigIntegerField()
    price = models.BigIntegerField()
    plate_number = models.BigIntegerField()
    bus_image = models.ImageField(upload_to='bus_image')
    max_volume = models.SmallIntegerField(default=50)
    TravelAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.bus_name} - {self.starting_point} to {self.destination}"
    
class BookingTickect(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    Bus = models.ForeignKey(SelamBusInfo,on_delete=models.CASCADE)
    payment_method = models.ImageField(upload_to='payment_methods')
    digital_id = models.ImageField(upload_to='user digital id')
    bocked_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.customer.first_name} - {self.customer.last_name}  from {self.Bus.starting_point} to {self.Bus.destination}"

class Announcement(models.Model):
    Title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='announcement')
    Description = models.TextField()
    Date = models.DateTimeField(default=timezone.now)  
    About = models.CharField(max_length=100,default='did not define')

    def __str__(self):
        return f"{self.Title}"
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=BookingTickect)
def update_bus_volume_on_approval(sender, instance, created, **kwargs):
    if not created:
        if instance.is_approved:
            bus = instance.Bus
            if bus.max_volume > 0:
                bus.max_volume -= 1
                bus.save()
             