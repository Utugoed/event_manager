from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from organisations.models import Organisation
from organisations.serializers import OrganisationSerializer


class OrganisationsAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        organisations = Organisation.objects.filter()
        serializer = OrganisationSerializer(organisations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "address": request.data.get("address"),
            "postcode": request.data.get("postcode"),
        }
        serializer = OrganisationSerializer(data=data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
