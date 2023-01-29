from django.db import models

# Create your models here.
class Property(models.Model):
    propertyName = models.CharField(max_length=100)
    totalRoom = models.IntegerField()
    propertyCapacity = models.IntegerField()
    address1 = models.TextField()
    address2 = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postCode = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    def create_user(self, propertyName, totalRoom,propertyCapacity,address1,address2,city,postCode,description,state,image):
        property = self.model(
            propertyName, 
            totalRoom,
            propertyCapacity,
            address1,
            address2,
            city,
            postCode,
            description,
            state,
            image
            )

        property.save(using=self._db)
        return property
    