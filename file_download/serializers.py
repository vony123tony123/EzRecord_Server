from rest_framework import serializers
from .models import MidiFileList

class MidiFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = MidiFileList
        field = '__all__'