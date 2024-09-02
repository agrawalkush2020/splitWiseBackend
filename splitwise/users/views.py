from django.http.response import HttpResponse
import json
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser

@csrf_exempt
def handle_signup(request):

    if request.method == "POST":
        credentials = json.loads(request.body)

        # Extract credentials
        username = credentials.get('userName')
        email = credentials.get('email')
        phone_number = credentials.get('phoneNumber')
        full_name = credentials.get('fullName')
        password = credentials.get('password')

        # Check if user already exists
        if CustomUser.is_existing_user(username=username, email=email, phone_number=phone_number):
            return HttpResponse(
                json.dumps({"success": False, "message": "User Already Exists!"}),
                content_type="application/json"
            )
            # Create new user
        new_user = CustomUser(
            username=username,
            email=email,
            phone_number=phone_number,
            full_name=full_name,
            password=make_password(password)  # Ensure you hash the password
        )
        new_user.save()
        return HttpResponse(
            json.dumps({"success": True, "message": "User created successfully!"}),
            content_type="application/json"
        )

    return HttpResponse(
        json.dumps({"success": False, "message": "Invalid request method"}),
        content_type="application/json"
    )


def handle_login(request):
    return HttpResponse(json.dumps({"success":True}),content_type="application/json")
    # return Response({'name':'kushagra'},status=status.HTTP_200_OK)