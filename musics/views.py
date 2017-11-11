from musics.models import Music
from musics.serializers import musicSerializer

from rest_framework import viewsets

# Authentications
from rest_framework.permissions import IsAuthenticated

# Parser
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = musicSerializer

    # DRF Authentications
    permission_classes = (IsAuthenticated,)

    # Allowed content type 
    # local setting (just in this class)
    # parser_classes = (JSONParser,)


     # /api/music/{pk}/detail/
    @detail_route(methods=['get'], url_path='detail_self')
    def detail(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }
        return Response(result, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def all_singer(self, request):
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)






