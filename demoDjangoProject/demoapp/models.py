from django.db import models

# Create your models here.
class Employee(models.Model):  # table name
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


# contacts
# name
# phone
# location
# email
# pin_code

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=13, null=False)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, null=False)
    pin_code = models.IntegerField(max_length=6, null=False)
    birth_date = models.DateField()

    def __str__(self):
        return "{name} - {phone}".format(name=self.name, phone=self.phone)





