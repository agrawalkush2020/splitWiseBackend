from django.http.response import HttpResponse
import json


def handle_signup(request):
    return HttpResponse(json.dumps({"success":True}),content_type="application/json")
    # return Response({'name':'kushagra'},status=status.HTTP_200_OK)


def handle_login(request):
    return HttpResponse(json.dumps({"success":True}),content_type="application/json")
    # return Response({'name':'kushagra'},status=status.HTTP_200_OK)