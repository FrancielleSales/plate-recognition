from rest_framework import serializers
from images.models.images import Images
import os

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['name', 'path', 'user']