from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reg(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    account_no = models.CharField(max_length=50, null='TRUE')
    firstname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    job= models.CharField(max_length=50)

    account_balance = models.IntegerField(default=0)
    account_pin = models.IntegerField(default=0000)
    
    dp = models.ImageField(null=True , blank=True, default="default.jpg", upload_to="ItemImage")
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.account_no


class Transfer(models.Model):
    counter = models.IntegerField(default=0)
    icon = models.CharField(max_length=50, default="up")
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=50, default="WIRE TRANSFER")
    amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Approved")  # You may remove this if not needed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mode= models.CharField(max_length=50, default="modal")


class History(models.Model):
    icon = models.CharField(max_length=50, default="up")
    color = models.CharField(max_length=50, default="green")
    date = models.DateTimeField()
    description = models.CharField(max_length=50, default="WIRE TRANSFER")
    amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Approved")  # You may remove this if not needed

    class Meta:
        ordering =['-date']

    def __str__(self):
        return self.description
