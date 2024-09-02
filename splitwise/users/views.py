from django.contrib.messages.api import success
from django.http.response import HttpResponse
from newrelic.packages.requests.models import json_dumps
from rest_framework.response import Response
from rest_framework import status


def handle_signup(request):
    return HttpResponse(json_dumps({"success":True}),content_type="application/json")
    # return Response({'name':'kushagra'},status=status.HTTP_200_OK)


def handle_login(request):
    return HttpResponse(json_dumps({"success":True}),content_type="application/json")
    # return Response({'name':'kushagra'},status=status.HTTP_200_OK)