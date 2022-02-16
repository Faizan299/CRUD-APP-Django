from django.db import models

class Student_Data(models.Model):
    id = models.IntegerField(primary_key=id)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        self.name
    
