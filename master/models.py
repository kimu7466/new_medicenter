from django.db import models
from .utils.genrate_unique_id import custom_filename
# Create your models here.
class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class CounterTable(BaseClass):
    last_staff_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Total staff : {self.last_staff_id}"
    

class doctor(BaseClass):
    DIR_NAME = 'doctors-profile'
    FILENAME_WORD = 'dp'
    profile = models.ImageField(upload_to=custom_filename, default='default_images\doctor-profile.png')
    name = models.CharField(max_length= 255)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name