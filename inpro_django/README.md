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
    
### What's next
 - Test the login/logout functionality
 - Add a navbar that contains login, logout, register functionality. As well as saying that the user is logged in
 - Restrict any access to the main pages of the website if the user is not logged in
 - Make the reset password functionality work
 - Add ability to add/update/delete a locker
 - Make the workflow of adding a new item to a locker easy. Thought needs to be put into this as if the user wants to add
an item for an itemType that does not exist, then they should be able to easily add a new ItemType. If the user wants to
add an Item for an ItemType that does exist, they should be presented with a list of avaiable item types

    
    
    