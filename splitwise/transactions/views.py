from http.client import HTTPResponse
from tokenize import group

from django.shortcuts import render
from .models import Transaction
from groups.models import Group
import json
from django.http.response import HttpResponse, JsonResponse

# Create your views here.

def fetch_all_transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(paid_by=user)


def fetch_all_transactions_by_gid(request):
    user = request.user
    credentials = json.loads(request.body)

    #to find the group
    group_name = credentials.get('groupName')
    group_instance = Group.objects.filter(name=group_name)



    transactions = Transaction.objects.filter(group=group_instance)

    return HttpResponse(json.dumps({"success": True, "transactions": transactions}),
                        content_type="application/json",
                        status=200)

