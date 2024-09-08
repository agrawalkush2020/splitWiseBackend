import uuid
from django.db import models
from users.models import CustomUser

class Group(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    # profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.name  # Corrected 'self.username' to 'self.name'

    class Meta:
        ordering = ['name']  # Example: order groups by name


class GroupMembership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # References Group model
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)    # References User model

    def __str__(self):
        return f'{self.user.username} in {self.group.name}'

    class Meta:
        unique_together = ('group', 'user')  # Ensures a user can't be added to the same group more than once