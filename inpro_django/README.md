### Useful tips and tricks while developing
In order to interact with the database, you can open up the python shell with the command:

    python manage.py shell
    
Then run the command:
    
    from inpro_home.models import (Locker, Item, ItemType)
    
Here are a few example commands for navigating the data present in the database:

    # Return all of the lockers:
    Locker.objects.all()
    
    # Create a new locker:
    locker = Locker(name="New Locker", address="Hyde Park")
    
    # Retrieve a single locker:
    locker = Locker.objects.filter(id=1).first()
    
    # Get all items of a locker
    lockerToQuery = Locker.objects.filter(id=1).first()
    itemInLocker = Item.obects.filter(locker=lockerToQuery) 
    
    
    