from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    # TODO (SAAS): Add an account field here so that InventoryPro can be used for multiple customers

    def __str__(self):
        return self.username
