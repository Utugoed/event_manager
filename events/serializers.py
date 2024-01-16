from rest_framework import serializers

from events.models import Event
from organisations.serializers import DetailedOrganisationSerializer


class EventSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Event
        fields = ["id", "title", "description", "organisations", "image", "date"]

class EventDetailSerializer(serializers.ModelSerializer):
    organisations = DetailedOrganisationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = ["id", "title", "description", "image", "date", "organisations"]