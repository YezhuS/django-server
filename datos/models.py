from django.db import models
from django.utils import timezone


class User(models.Model):
  # Campos
  objects = models.Manager()

  name = models.CharField(max_length=20) 
  email = models.EmailField(max_length=200)

 

class Note(models.Model):
  # Campos
  objects   = models.Manager()

  note      = models.TextField(max_length=200)
  date      = models.DateTimeField(auto_now_add=True)
  end_date  = models.DateTimeField(default=timezone.now)
  adjunto   = models.FileField(upload_to='uploads/', blank=True, null=True)
  user      = models.ForeignKey(User, on_delete=models.CASCADE)
  task      = models.BooleanField()
  tag       = models.CharField(max_length=20, blank=True, null= True)

  Agua      = 'Agua'
  Fuego     = 'Fuego'
  Planta    = 'Planta'
  TYPES      = [
    (Agua, 'Agua'),
    (Fuego, 'Fuego'),
    (Planta, 'Planta'),
  ]
  type      = models.CharField(max_length=10, choices=TYPES)
