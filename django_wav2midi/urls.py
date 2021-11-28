"""django_wav2midi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from file_upload import file_upload_views
from wav2midi import wav2midi_views
from file_download import file_download_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file_upload/', file_upload_views.UploadView.as_view()),
    path('wav2midi/', wav2midi_views.wav2midi.as_view()),
    path('file_download/',file_download_views.DownloadView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# urlpatterns = format_suffix_patterns(urlpatterns)