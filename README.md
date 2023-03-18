# Django-Project

i make project according to this model or input commands:

Create an api to insert data and retrieve data.
Data would be username, firstname, lastname, pincode, email.


Insert User metadata
Request:
	POST /api/user/v1/public/user_metadata

	request body:
		{
			"username" : "jdoe",
			"firstname" : "John",
			"lastname" : "doe",
			"pincode" : "213452",
			"email" : "john.doe@gmail.com",
		}

Username should be unique


Get User metadata

Response: 204 No content

	GET /api/user/v1/public/user_metadata?username=jdoe


Respone: 200 OK 
Response Body:
	{
		"username" : "jdoe",
		"firstname" : "John",
		"lastname" : "doe",
		"pincode" : "213452",
		"email" : "john.doe@gmail.com",
	}

It should have proper methods and naming convention should be followed.
Object oriented programming is required.
You can create table named UserMetadata. 
You can choose any web framework to implement. Django or fastAPI is preferrable.
-------------------------------------------------------------------------------------------
In this i also add some extra functionality like put/patch/delete.
you can use postman api tool for access to this functions.

for reference youtube will be very useful.
youtube link:https://www.youtube.com/watch?v=0jR5UFsAHkU&t=1689s

used model is(models.py):
from django.db import models

# Create your models here.

class Employee(models.Model):
    username =models.CharField(max_length=50)
    fname =models.CharField(max_length=50)
    lname =models.CharField(max_length=50)
    pincode = models.IntegerField(null=True)
    email =models.EmailField(db_index=True,unique=True,max_length=50)

---------------------------------------------------------------------------------------------
other references:
https://www.djangoproject.com/start/
https://www.youtube.com/watch?v=ejJ-2oz4AgI

