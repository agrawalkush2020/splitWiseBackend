import uuid
from django.db import models
from users.models import CustomUser
from groups.models import Group

# Create your models here.


class Transaction(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    paid_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='paid_by')  # Link to CustomUser model
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='transactions')  # Link to Group model
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Define amount with precision
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date to now when creating a new object
    paid_to = models.ManyToManyField(CustomUser, related_name='paid_to') # Many-to-many relationship with CustomUser

    def __str__(self):
        return f'Transaction by {self.paid_by.username} for group {self.group.name}'
