from django.forms import  ModelForm
from brake_secure.models import RPack

class RPackForm(ModelForm):
    class Meta:
        model = RPack
        fields = ['name', 'description', 'author', 'maintainer', 'keywords', 'cranLink', 'website', 'versionMajor',
                  'versionMinor', 'versionPatch', 'versionBuild', 'approved','last_version_date']
