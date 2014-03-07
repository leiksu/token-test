from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from models import ClientData
import json
import uuid
 
def register_app(request):
    """
    When a client application calls this API, it should receive a unique token which it 
    should then include with any other request. This token will be used to identify the 
    application to the web service.
    """
    
    token = uuid.uuid4().hex
    my_json_data = json.dumps(token)
    return HttpResponse(my_json_data, content_type="application/json")

def store_data(request, token, key, value):
    """
    This API should accept three parameters:
        a. The client's unique registration token
        b. A key name which should be a string between 1 and 20 characters long
        c. A value which should be a string between 0 and 100 characters long

    The web service should store the key and value against the client record for future retrieval
    """
    
    clientdata = ClientData(
                            token = token,
                            client_key = key,
                            client_value = value
                            )

    clientdata.save()
    
    html="<html><body><span>the client data is stored</span></body></html>"
    return HttpResponse(html)
    
    
def retrieve_data(request, token, key=None):
    """
    This API should accept the following parameters:
        a. The client's unique registration token
        b. An optional key name which should be a string between 1 and 20 characters long

    If the key name is supplied and that key has been stored against the identified client, 
    the API should return the related value.

    If the key name is not supplied, all key/value pairs for the identified client should be 
    returned.
    """
    
        
    clientdata = ClientData.objects.get(token=token)
    template = get_template("token_api/clientdata_view.html")
    
    
    variables = Context({
                         'client_key': key,
                         'client_value': clientdata.client_value                        
                         })

    return HttpResponse( template.render(variables) )
    
    
    