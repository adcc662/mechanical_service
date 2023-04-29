from django.db import models

# Create your models here.

class Customer(models.Model):
    """This class represents the customer model."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    detail = models.TextField()
    insert_ts = models.DateTimeField(auto_now_add=True)


class ContactType(models.Model):
    """This class represents the contact type model."""
    type_name = models.CharField(max_length=50)    


class Contact(models.Model):
    """This class represents the contact model."""
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_type_id = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    contact_detail = models.TextField()
    insert_ts = models.DateTimeField(auto_now_add=True)

