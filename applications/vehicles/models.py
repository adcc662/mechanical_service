from django.db import models
from applications.customers.models import Customer


class VehicleType(models.Model):
    """This class represents the vehicle type model."""
    type_name = models.CharField(max_length=50)


class ModelVehicle(models.Model):
    """This class represents the vehicle model."""
    model_name = models.CharField(max_length=50)
    vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)


class Vehicle(models.Model):
    """This class represents the vehicle information."""
    vin = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    model_id = models.ForeignKey(ModelVehicle, on_delete=models.CASCADE)
    year = models.IntegerField()
    detail = models.TextField()
    insert_ts = models.DateTimeField(auto_now_add=True)


class Model(models.Model):
    """This class represents the vehicle model."""
    model_name = models.CharField(max_length=50)
    vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    make_id = models.ForeignKey('Make', on_delete=models.CASCADE)


class Make(models.Model):
    """This class represents the vehicle make."""
    make_name = models.CharField(max_length=50)


