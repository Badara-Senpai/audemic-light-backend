from django.urls import path
from .views import FileUploadView, ExtractTextView, RecentFilesList

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('extract-text/<int:pk>/', ExtractTextView.as_view(), name='extract-text'),
    path('recent-files/', RecentFilesList.as_view(), name='recent-files'),
]
