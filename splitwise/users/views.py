from rest_framework.response import Response
from rest_framework import status

def handle_signup(request):
    return Response({'name':'kushagra'},status=status.HTTP_200_OK)


def handle_login(request):
    return Response({'name':'kushagra'},status=status.HTTP_200_OK)