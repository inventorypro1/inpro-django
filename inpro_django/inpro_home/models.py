from django.db import models

class Locker(models.Model):
    name = models.CharField(max_length=100)
    # TODO: Make this into a django-address field
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Used to store the various types of items that a customer has
class ItemType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Used to store an instance of an ItemType in a locker
class Item(models.Model):
    itemType = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.itemType.name + " item"

    class Meta:
        unique_together = ('itemType', 'locker')

