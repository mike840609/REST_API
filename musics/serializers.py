from rest_framework import serializers
from musics.models import Music

class musicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        # fields = ('id','song','singer','last_modify_date','created')
