from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid


class User(models.Model):
    """Model representing a user genre."""
    # FIELDS
    first_name = models.CharField(max_length=20, help_text="First Name", verbose_name="First Name", default="")
    last_name = models.CharField(max_length=20, help_text="Last Name", verbose_name="Last Name", default="")
    email = models.EmailField(max_length=100, help_text="Email", verbose_name="Email ID", default="")
    password = models.CharField(max_length=20, help_text="Password", verbose_name="Password", default="")
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                               help_text='Unique ID for this particular user across '
                                         'whole library')
    shopping_cart = models.IntegerField(help_text="shopping cart/bundle id", verbose_name="Shopping Cart", default="")

    # METHODS
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    # CREATE A NEW RECORD OF USER
    def make_user(self):
        record = User(self.first_name, self.last_name, self.email, self.password, self.id, self.shopping_cart)
        record.save()

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_user_id(self):
        return self.user_id

    def get_shopping_cart(self):
        return self.shopping_cart


class Item(models.Model):
    """Model representing an item."""
    # FIELDS
    product_name = models.CharField(max_length=200, help_text='product name', verbose_name="Product Name", default="")
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular '
                                                                                  'product across whole library')

    index = models.IntegerField(default=0, help_text='index', verbose_name="Index")
    price = models.IntegerField(default=0, help_text='product id', verbose_name="Product ID")
    img = models.CharField(max_length=100, help_text='image', verbose_name="Image", default="")

    # METHODS
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Item."""
        return reverse('model-detail-view', args=[str(self.product_id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.product_name

    def get_name(self):
        return self.product_name

    def get_price(self):
        return self.price

    def get_product_id(self):
        return self.product_id

    def get_index(self):
        return self.index


class Size(models.Model):
    name = models.CharField(max_length=200, help_text='Size name', verbose_name="Size Name", default="")
    img = models.CharField(max_length=200, help_text='image', verbose_name="Image", default="")

    def get_name(self):
        """String for representing the Model object."""
        return self.name

    def get_img(self):
        return self.img


class Season(models.Model):
    name = models.CharField(max_length=200, help_text='Season name', verbose_name="Season Name", default="")
    img = models.CharField(max_length=200, help_text='image', verbose_name="Image", default="")

    def get_name(self):
        """String for representing the Model object."""
        return self.name

    def get_img(self):
        return self.img


class Bundle(models.Model):
    bundle_id = models.IntegerField(help_text="model id", verbose_name="Model ID", default=0)
    # items_list = models.ListCharFields(base_field=Item)
    shirt_quantity = models.IntegerField(help_text="quantity of shirts", verbose_name="Quantity", default=0)
    pants_quantity = models.IntegerField(help_text="quantity of pants", verbose_name="Quantity", default=0)
    dress_quantity = models.IntegerField(help_text="quantity of dresses", verbose_name="Quantity", default=0)
    shoes_quantity = models.IntegerField(help_text="quantity of shoes", verbose_name="Quantity", default=0)
    socks_quantity = models.IntegerField(help_text="quantity of socks", verbose_name="Quantity", default=0)
    onesie_quantity = models.IntegerField(help_text="quantity of onesie", verbose_name="Quantity", default=0)
    total = models.IntegerField(help_text="total price", verbose_name="Total Price", default=0)

    def add_item(self, other):
        if other.get_name() == "shirt":
            self.shirt_quantity += 1
        elif other.get_name() == "pants":
            self.pants_quantity += 1
        elif other.get_name() == "socks":
            self.socks_quantity += 1
        elif other.get_name() == "shoes":
            self.shoes_quantity += 1
        elif other.get_name() == "dress":
            self.dress_quantity += 1
        elif other.get_name() == "onesie":
            self.onesie_quantity += 1
        self.total += other.get_price()

    def remove_item(self, other):
        if other.get_name() == "shirt":
            self.shirt_quantity -= 1
        elif other.get_name() == "pants":
            self.pants_quantity -= 1
        elif other.get_name() == "socks":
            self.socks_quantity -= 1
        elif other.get_name() == "shoes":
            self.shoes_quantity -= 1
        elif other.get_name() == "dress":
            self.dress_quantity -= 1
        elif other.get_name() == "onesie":
            self.onesie_quantity -= 1
        self.total += other.get_price()

    def get_bundle_id(self):
        return self.bundle_id

    def get_total(self):
        return self.total

    def get_shirt_quantity(self):
        return self.shirt_quantity

    def get_pants_quantity(self):
        return self.pants_quantity

    def get_dress_quantity(self):
        return self.dress_quantity

    def get_socks_quantity(self):
        return self.socks_quantity

    def get_shoes_quantity(self):
        return self.shoes_quantity

    def get_onesie_quantity(self):
        return self.onesie_quantity
