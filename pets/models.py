from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Pet(models.Model):
    GENDER_CHOICE = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('Other', 'Other'),
        ('not_mentioned', 'Prefer Not to Say')
    ]
    name = models.CharField(max_length=300)
    age  = models.PositiveSmallIntegerField(verbose_name='Pet age', validators=[MinValueValidator(0), MaxValueValidator(800)])
    description = models.TextField()
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    color = models.CharField(max_length=100, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)

class PetInfo(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    routine = models.TextField(null=True, blank=True)
    eating_habits = models.TextField(null=True, blank=True)
    play_time = models.CharField(max_length=100, null=True, blank=True)
    wake_up_time = models.CharField(max_length=100, null=True, blank=True)
    sleep_up_time = models.CharField(max_length=100, null=True, blank=True)
    behavior = models.CharField(max_length=100, blank=True, null=True)
    special_needs = models.TextField(null=True, blank=True) 

class PetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    breed = models.CharField(max_length=100, null=True, blank=False)
    species = models.CharField(max_length=100, null=False, blank=False)
    habitat = models.CharField(max_length = 100, null=True, blank=True)
    temperament = models.TextField(null=True, blank=True)
    excercise_needs = models.TextField(null=True, blank=True)
    idea_environment = models.TextField(null=True, blank=True)
    care_instructions = models.TextField(null=True, blank=True)
    
class PetBelonging(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    dimensions = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

class PetBelongingsImage(models.Model):
    pet = models.ForeignKey(PetBelonging, on_delete=models.CASCADE)
    resource_link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)

class PetMedia(models.Model):
    RESOURCE_TYPES = [
        ('audio', 'Voice'),
        ('image', 'Picture'),
        ('video', 'Video')
    ]
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    resource_link = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True)
