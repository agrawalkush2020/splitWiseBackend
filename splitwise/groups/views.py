import json
from .models import Group,GroupMembership
from django.http.response import HttpResponse

# Create your views here.


def get_group_list(request):
    user = request.user

    # Get all groups where the logged-in user is a member
    memberships = GroupMembership.objects.filter(user=user)
    groups = [membership.group for membership in memberships]

    return HttpResponse(json.dumps({"success": True, "groups": groups}), content_type="application/json")

def make_group(request):
    user = request.user

    if request.method == "POST":
        credentials = json.loads(request.body)

        # Extract credentials
        name = credentials.get('groupName')
        user_names = credentials.get('userNames')









