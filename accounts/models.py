from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

class Profile(models.Model):
    # TODO: add dob check if its valid or not
    ROLE_CHOICE = [
        ('giver', 'Pet Giver'),
        ('borrower', 'Pet Borrower'),
        ('Seller', 'Pet Seller'),
        ('daycare', 'Daycare provider'),
    ]
    GENDER_CHOICE = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('Other', 'Other'),
        ('not_mentioned', 'Prefer Not to Say')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    roles = models.CharField(max_length=10, choices=ROLE_CHOICE)
    picture = models.CharField(max_length=500)
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=False, blank=False, validators=[MinValueValidator(16), MaxValueValidator(100)])
    date_of_birth = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)


    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

class Address(models.Model):
    address = models.TextField(verbose_name='Address', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Country')
    state = models.CharField(max_length=100, verbose_name='State')
    city = models.CharField(max_length=100, verbose_name='City')
    zipcode = models.CharField(max_length=20, verbose_name='Zipcode')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')

    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)
