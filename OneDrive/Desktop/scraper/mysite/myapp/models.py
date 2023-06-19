from django.db import models

# Create your models here.

class Link(models.Model):

    def __str__(self):
        return self.name

    address = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)

# writing "null=true" above is very necessary because some links may not have a proper address.
# We therefore write "null=true" in order to avoid any errors