from musics.models import Music
from musics.serializers import musicSerializer

from rest_framework import viewsets

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = musicSerializer
