import json
from .models import Group,GroupMembership
from django.http.response import HttpResponse, JsonResponse
from users.models import CustomUser

# Create your views here.


def get_group_list(request):
    user = request.user

    # Get all groups where the logged-in user is a member
    memberships = GroupMembership.objects.filter(user=user)
    groups = [membership.group for membership in memberships]

    return HttpResponse(json.dumps({"success": True, "groups": groups}), content_type="application/json")

def make_group(request):
    user = request.user

    # if request POST method ki ni hai toh
    if request.method != 'POST':
        return HttpResponse(status=404)

    credentials = json.loads(request.body)
    group_name = credentials.get('groupName')
    user_names = credentials.get('userNames')

    # Create a new group
    new_group = Group.objects.create(name=group_name)

    for names in user_names:
        user_object = CustomUser.objects.get(username=names)
        group_membership = GroupMembership.objects.create(group=new_group, user=user_object)

    return JsonResponse({'success': True}, status=200)











