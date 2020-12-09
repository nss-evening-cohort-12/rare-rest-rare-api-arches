import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rareserverapi.models import RareUsers

@csrf_exempt
def register_user(request):

    # incoming Json string
    req_body = json.loads(request.body.decode())

    #check if user exists in db
    user_exists = User.objects.filter(email=req_body['email']).exists()

    if user_exists:
      data = json.dumps({"msg": "user already exists"})
      return HttpResponse(data, content_type='application/json')
      
    # invoke Djangos built in user model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        is_staff=True
    )

    # Add extra info to RareUsers table
    rareUser = RareUsers.objects.create(
        bio=req_body['bio'],
        profile_image_url=req_body['profile_image_url'],
        active=True,
        user=new_user
    )

    # Commit the user to the database by saving it
    rareUser.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')
