from djongo import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Category(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    objects = models.DjongoManager()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    amount_in_stock = models.IntegerField()
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    category = models.EmbeddedField(
        model_container=Category,
        )
    objects = models.DjongoManager()

    def __str__(self):
        return self.name