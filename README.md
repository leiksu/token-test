This is a stand-alone web service that is accessed by various client applications to store and retrieve simple key/value pairs.

Each client application has its own set of key/value pairs that can only be accessed by itself.

The web service has three APIs:

1. Register Application.

  When a client application calls this API, it receives a unique token which it includes with any other request. This token is used to identify the application to the web service.

2. Store data 

  This API accepts three parameters: 
  a. The client's unique registration token 
  b. A key name which should be a string between 1 and 20 characters long 
  c. A value which should be a string between 0 and 100 characters long

  The web service stores the key and value against the client record for future retrieval

3. Retrieve data 

  This API accepts the following parameters: 
  a. The client's unique registration token 
  b. An optional key name which is a string between 1 and 20 characters long

  If the key name is supplied and that key has been stored against the identified client, the API returns the related value.  
  If the key name is not supplied, all key/value pairs for the identified client is returned.  

  The data stored in sqlite persists after the web service is stopped and is available once it is restarted.
