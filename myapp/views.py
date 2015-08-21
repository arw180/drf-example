import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import django.contrib.auth

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

import myapp.serializers as serializers
import myapp.models as models


# Get an instance of a logger
logger = logging.getLogger('mylogger')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = django.contrib.auth.models.User.objects.all()
    serializer_class = serializers.ShortUserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ListingViewSet(viewsets.ModelViewSet):
    logger.info('inside ListingSerializerViewSet')
    queryset = models.Listing.objects.all()
    serializer_class = serializers.ListingSerializer

    def create(self, request):
        logger.info('inside ListingViewSet.create')
        serializer = serializers.ListingSerializer(data=request.data,
            context={'request': request}, partial=True)
        if not serializer.is_valid():
            logger.error('%s' % serializer.errors)
            return Response(serializer.errors,
                  status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

