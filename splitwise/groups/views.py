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






