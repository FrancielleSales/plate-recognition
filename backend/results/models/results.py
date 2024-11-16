from django.db import models
from users.models.users import User
from images.models.images import Images

class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

    x_min = models.FloatField()
    y_min = models.FloatField()
    x_max = models.FloatField()
    y_max = models.FloatField()

    points_precision = models.FloatField()
    license_plate = models.CharField(max_length=7)
    plate_precision = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result {self.id} for User {self.user_id} on Image {self.image_id}"

    class Meta:
        db_table = 'results'
