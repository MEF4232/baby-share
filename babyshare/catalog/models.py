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
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Category(models.Model):
    """Model representing the category."""
    name = models.CharField(max_length=200, help_text='Enter the item category.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    # TODO Add to Item:
    # category = models.ManyToManyField(Category, help_text='Select a category for this item')

class Subcategory(models.Model):
    """Model representing the subcategory."""
    name = models.CharField(max_length=200, help_text='Enter the item subcategory.')
    
    category = models.ManyToManyField(Category, help_text='Select a category for this item')
   
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    # TODO Add to Item:
    # subcategory = models.ManyToManyField(Subcategory, help_text='Select a subcategory for this item')
