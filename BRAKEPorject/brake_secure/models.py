from django.db import models
from django.contrib.auth.models import User

class RPack( models.Model ):
    name = models.CharField( max_length = 100)
    description = models.TextField( blank = True )
    user = models.ForeignKey( User, on_delete= models.CASCADE ) # User that the package belongs do in this system, eg the owner of this recor
    last_version_date = models.DateTimeField( null=True, blank = True)
    created = models.DateTimeField( auto_now_add=True)  # This is the date the record was added and is not something we can change, set automatically

    def __str__(self):
        return self.name
