from musics.models import Music
from musics.serializers import musicSerializer

from rest_framework import viewsets

# Authentications
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = musicSerializer

    # DRF Authentications
    permission_classes = (IsAuthenticated,)

    # Allowed content type 
    # local setting (just in this class)
    parser_classes = (JSONParser,)

