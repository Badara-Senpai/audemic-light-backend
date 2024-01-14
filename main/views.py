from django.http import Http404
from rest_framework.views import APIView
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from .utils import extract_text_from_pdf


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()

            file_path = file_serializer.validated_data['file'].path

            text = extract_text_from_pdf(file_path)

            return Response({'file': file_serializer.data, 'text': text}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecentFilesList(generics.ListAPIView):
    queryset = UploadedFile.objects.all().order_by('-uploaded_at')[:10]
    serializer_class = UploadedFileSerializer


class ExtractTextView(APIView):
    def get_object(self, pk):
        try:
            return UploadedFile.objects.get(pk=pk)
        except UploadedFile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        uploaded_file = self.get_object(pk)
        text = extract_text_from_pdf(uploaded_file.file.path)

        return Response({'text': text})
