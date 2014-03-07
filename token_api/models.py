from django.db import models

class ClientData(models.Model):
    """
    store and retrieve data of client application
    """
    token = models.CharField(max_length=50)
    client_key = models.CharField(max_length=20)
    client_value = models.CharField(max_length=100)
    
    def __unicode__(self): 
        return self.token + " : " + self.client_key + " , " + self.client_value