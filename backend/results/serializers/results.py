from rest_framework import serializers
from results.models.results import Results

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['id', 'user', 'image', 'x_min', 'y_min', 'x_max', 'y_max', 'points_precision', 'license_plate', 'plate_precision', 'created_at']
