from django.contrib import admin
from .models import (
    Locker,
    ItemType,
    Item,
)

admin.site.register(Locker)
admin.site.register(ItemType)
admin.site.register(Item)
