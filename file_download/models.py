from django.db import models

# Create your models here.
class MidiFileList(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'MidiFileList'