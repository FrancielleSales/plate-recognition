from django.db import models
from users.models.users import User

class Images(models.Model):
    name = models.CharField(max_length=50, unique=True)
    path = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.name