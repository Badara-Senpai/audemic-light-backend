from rest_framework import serializers
from .models import UploadedFile
import os


class UploadedFileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at', 'file_name']

    def get_file_name(self, obj):
        return os.path.basename(obj.file.name)
