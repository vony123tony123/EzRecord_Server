from rest_framework import serializers
from .models import RecordFileList

class RecordFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = RecordFileList
        field = '__all__'
