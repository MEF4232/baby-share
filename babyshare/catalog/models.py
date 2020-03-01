from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid


class User(models.Model):
    """Model representing a user genre."""
    # FIELDS
    first_name = models.CharField(max_length=20, help_text="First Name", verbose_name="First Name")
    last_name = models.CharField(max_length=20, help_text="Last Name", verbose_name="Last Name")
    email = models.EmailField(max_length=100, help_text="Email", verbose_name="Email ID")
    password = models.CharField(max_length=20, help_text="Password", verbose_name="Password")

    # METHODS
    def __str__(self):
        """String for representing the Model object."""
        name = str(self.first_name) + " " + str(self.last_name)
        return name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.__str__())])

    # CREATE A NEW RECORD
    record = User(first_name, last_name, email, password)
    record.save()


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
    # category = models.ManyToManyField(Category, help_text='Select a category for this item')git

class Subcategory(models.Model):
    """Model representing the subcategory."""
    name = models.CharField(max_length=200, help_text='Enter the item subcategory.')
    
    category = models.ManyToManyField(Category, help_text='Select a category for this item')
   
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    # TODO Add to Item:
    # subcategory = models.ManyToManyField(Subcategory, help_text='Select a subcategory for this item')
