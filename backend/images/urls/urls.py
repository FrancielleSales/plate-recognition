from django.urls import path
from images.views.images import ImagesView

urlpatterns = [
    path('process/', ImagesView.as_view(), name='process_image'),
]