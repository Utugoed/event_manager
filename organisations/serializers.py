from rest_framework import serializers

from organisations.models import Organisation
from users.models import CustomUser
from users.serializers import UserSerializer

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ["title", "description", "address", "postcode"]

class DetailedOrganisationSerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()
    
    def get_full_address(self, organisation):
        return f"{organisation.address} {organisation.postcode}"
    
    def get_members(self, organisation):
        users = CustomUser.objects.filter(organisation=organisation)
        users = users.filter(is_active=True)
        serializer = UserSerializer(users, many=True)
        return serializer.data

    class Meta:
        model = Organisation
        fields = ["title", "description", "full_address", "members"]
    