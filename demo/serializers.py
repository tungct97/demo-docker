from rest_framework import serializers

from demo.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('name', 'description')
