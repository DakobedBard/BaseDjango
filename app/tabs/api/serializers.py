from rest_framework import serializers
from tabs.models import GuitarTab

class GuitarTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuitarTab
        fields = [
            'title',
            'audio_file_path',
            'bucket',
        ]