from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('courier', 'Courier'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')

class Parcel(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    sender = models.ForeignKey(CustomUser, related_name='sent_parcels', on_delete=models.CASCADE)
    reciever_name = models.CharField(max_length=255)
    receiver_address = models.TextField()
    courier = models.ForeignKey(CustomUser, related_name='courier_parcels', on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    
class DeliveryProof(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE, related_name='delivery_proof')
    image = models.ImageField(upload_to='delivery_proofs/')
    timestamp = models.DateTimeField(auto_now_add=True)