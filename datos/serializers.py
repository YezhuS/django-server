from rest_framework import serializers
from .models import Note
from .models import User


class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__' 