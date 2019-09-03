import uuid # Required for unique car instances

from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class CarBrand(models.Model):
    """Model representing a car's brand/manufacturer"""       
    name = models.CharField(max_length=200, help_text='Enter a car brand (e.g. Toyota)')
    logo = models.ImageField(upload_to='media/images/logos', help_text='Upload brand logo')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    # def display_quantity(self):
    #     """Should return the quantity of cars of this brand(e.g all Toyota cars)"""
    #     return self.__class__.objects.count()

    # display_quantity.short_description = 'Quantity'


class CarModel(models.Model):
    """Model representing a car (but not a specific copy of a car)."""
    name = models.CharField(max_length=200)

    # Foreign Key used because car can only have one brand, but brands can have multiple cars
    # car as a string rather than object because it hasn't been declared yet in the file
    brand = models.ForeignKey('CarBrand', on_delete=models.SET_NULL, null=True, help_text='Enter the specific model of the car')
    price = models.IntegerField(help_text='Enter price of the car')
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the car')
    
    photo = models.ImageField(upload_to='media/images/cars', help_text='Upload the image of the car')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this car."""
        return reverse('car-detail', args=[str(self.id)])
    
    # def display_quantity(self):
    #     """Return the quantity of a specific car's instances e.g All Toyota Corolla cars"""
    #     return self.__class__.objects.count()

    # display_quantity.short_description = 'Quantity'


class CarModelInstance(models.Model):
    """Model representing a specific copy of a car (i.e. that can be bought from the shop)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular car across whole shop')
    car = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True)

    PURCHASE_STATUS = (
        ('a', 'Available'),
        ('s', 'Sold Out'),
    )

    status = models.CharField(
        max_length=1,
        choices=PURCHASE_STATUS,
        blank=True,
        default='s',
        help_text='Car availability',
    )

    class Meta:
        ordering = ['status']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.car.name})'