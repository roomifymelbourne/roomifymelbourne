from django.db import models

# Create your models here.

class UserForm(models.Model):
    name = models.CharField(max_length=250)
    mail = models.EmailField(max_length=250)
    phno = models.CharField(max_length=15)  # Updated to CharField
    rent = models.DecimalField(max_digits=10, decimal_places=2)  # Or IntegerField if it's an integer
    city = models.CharField(max_length=250)
    university = models.CharField(max_length=250)


    def __str__(self):
          return self.name
    

class EnquiryForm(models.Model):
     whatsapp = models.CharField(max_length=250)


     def __str__(self):
          return self.whatsapp    