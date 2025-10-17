from django.db import models
# Create your models here.
class Equipment(models.Model):
# each class variable represents a database i.e. table field in the model
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    localtion = models.CharField(max_length=30)
    eir_code = models.CharField(max_length=7)
    create_date = models.DateTimeField('create date')
    create_by = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

def __str__(self):
    return self.name + " - " + self.status
