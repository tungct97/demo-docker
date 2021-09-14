from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from demo.models import Note
from rest_framework import viewsets, status

from demo.serializers import NoteSerializer
from demodocker.middlewares.authentication import Authentication


class NoteViewSet(viewsets.ViewSet):
    authentication_classes = [Authentication]

    @swagger_auto_schema(request_body=NoteSerializer)
    def create(self, request, *args, **kwargs):
        note_serializer = NoteSerializer(data=request.data)
        if note_serializer.is_valid():
            note_serializer.save(user=request.user)
            return Response({}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        notes = Note.objects.filter(user=request.user)
        response = [
            {'id': note.id, 'name': note.name, 'description': note.description}
            for note in notes
        ]
        
        return Response(response, status=status.HTTP_201_CREATED)
