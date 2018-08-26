from django.db import models

# Create your models here.


class Name(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    def getfirstname(self):
        return self.firstname

    def getlastname(self):
        return self.lastname

    def getfullname(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
