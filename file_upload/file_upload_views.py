from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import RecordFileList
from .serializers import RecordFileSerializers

# Create your views here.
class UploadView(APIView):
    def get(self,request):
        RecordFiles = RecordFileList.objects.all()
        serializer = RecordFileSerializers(RecordFiles,many=True)
        return Response(serializer.data)

    def post(self,request):
        if request.FILES['RecordFile']:
            print(request.FILES['RecordFile'].__dict__)
            recordfile = request.FILES['RecordFile']
            fs = FileSystemStorage()
            filename = fs.save(recordfile.name, recordfile)
            uploaded_file_url = fs.url(filename)
            path = fs.location + '/' + filename
            RecordFileList.objects.create(name=filename,path=path)
            return HttpResponse(path)
