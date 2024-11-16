from rest_framework import serializers
from results.models.results import Results

class ResultsSerializer(serializers.ModelSerializer):
    image_name = serializers.CharField(source='image.name')

    class Meta:
        model = Results
        fields = ['id', 'user', 'image', 'image_name', 'x_min', 'y_min', 'x_max', 'y_max', 'points_precision', 'license_plate', 'plate_precision', 'created_at']
