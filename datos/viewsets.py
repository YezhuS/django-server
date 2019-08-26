from rest_framework import viewsets
from .models import Note
from .models import User
from .serializers import NoteSerializer
from .serializers import UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer