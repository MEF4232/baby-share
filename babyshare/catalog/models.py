from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid

class User(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Item(models.Model):
    """Model representing an item."""
    # Fields
    product_name = models.CharField(max_length=200, help_text='Enter a product name')
    product_id = models.IntegerField()
    price = models.FloatField()

    # Create Record (Item)
    record = Item(product_name, product_id, price)
    record.save()

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.product_id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.product_name


class Inventory(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

