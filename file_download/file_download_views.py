import os

from django.http import FileResponse
from django.shortcuts import render
from rest_framework.views import APIView
import os;


class DownloadView(APIView):
    def post(self,request):
        midpath = request.POST.get('filepath')
        response = FileResponse(open(midpath,'rb'))
        response['content_type'] = 'audio/mid'
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(midpath)
        os.remove(midpath)
        return response