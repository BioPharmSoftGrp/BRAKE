from django.db import models
from django.contrib.auth.models import User

class RPack( models.Model ):
    created = models.DateTimeField( auto_now_add=True)  # This is the date the record was added and is not something we can change, set automatically
    name = models.CharField( max_length = 100)
    description = models.TextField( blank = True )
    autor = models.TextField( blank = True )
    maintainer = models.TextField( blank = True )
    keywords = models.TextField( blank = True )
    cranLink = models.URLField( blank = True )
    website = models.URLField( blank = True )

    versionMajor = models.IntegerField( default = 0 )
    versionMinor =  models.IntegerField(  default = 0)
    versionPatch = models.IntegerField( default = 0 )
    versionBuild = models.IntegerField( default = 0)

    approved = models.BooleanField(  default = False)                     # Whenever a new package is added somone needs to reveiw and approve
    user = models.ForeignKey( User, on_delete= models.CASCADE ) # User that the package belongs do in this system, eg the owner of this recor
    last_version_date = models.DateTimeField( null=True, blank = True)

    def __str__(self):
        return self.name + " - " + self.description

    def versionString( self ):
        if self.versionBuild == 0:
            strBuild = ""
        else:
            strBuild = ".%s" % ( self.versionBuild)
        strVersion = "%s.%s.%s%s" % ( self.versionMajor, self.versionMinor, self.versionPatch,strBuild)
        return strVersion
