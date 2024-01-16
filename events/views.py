import asyncio
import json
from time import sleep

from asgiref.sync import sync_to_async

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.models import Event
from events.serializers import EventSerializer, EventDetailSerializer


class EventListView(APIView):
    permission_classes = (IsAuthenticated, )

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def events_list(request, *args, **kwargs):
    title_query = request.query_params.get('title', '')
    date_query = request.query_params.get('date', '')
    order = request.query_params.get('order')
    limit = request.query_params.get('limit')
    offset = request.query_params.get('offset')

    queryset = Event.objects.all()

    if (title_query):
        queryset = queryset.filter(title__icontains=title_query)
    
    if (date_query):
        queryset = queryset.filter(date=date_query)
    
    if (order in ("asc", "desc")):
        order_by = ('-' if order == 'desc' else '') + "date"
        queryset = queryset.order_by(order_by)
        

    if limit is not None:
        paginator = LimitOffsetPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = EventSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = EventSerializer(queryset, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_event(request, *args, **kwargs):
    try:
        event = Event.objects.get(id=kwargs["id"])
    except Event.DoesNotExist as ex:
        return Response({"error": "Not found"}, status=HTTP_404_NOT_FOUND)
    
    serializer = EventDetailSerializer(event)
    return Response(serializer.data, status=HTTP_200_OK)

@sync_to_async
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request, *args, **kwargs):
    data = {
        "title": request.data.get("title"),
        "description": request.data.get("description"),
        "organisations": json.loads(request.data.get("organisations")),
        "image": request.data.get("image"),
        "date": request.data.get("date")
    }
    serializer = EventSerializer(data=data)

    sleep(60)

    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
