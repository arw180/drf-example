import logging

import django.contrib.auth

from rest_framework import serializers

import myapp.models as models
import myapp.model_access as model_access

logger = logging.getLogger('mylogger')

class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ('username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer()
    class Meta:
        model = models.Profile
        fields = ('user', 'display_name')
        read_only = ('display_name',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'description')
        read_only = ('description',)

        extra_kwargs = {
            'name': {
                'validators': []
            }
        }


class ListingSerializer(serializers.ModelSerializer):
    owners = ProfileSerializer(required=False, many=True)
    category = CategorySerializer(required=False)
    # category = serializers.SlugRelatedField(
    #     slug_field='category.name',
    #     queryset=models.Category.objects.all()
    # )

    class Meta:
        model = models.Listing
        depth = 2

    def validate(self, data):
        logger.info('inside ListingSerializer validate')
        data['category'] = models.Category.objects.get(name=data['category']['name'])
        return data

    def create(self, validated_data):
        logger.info('inside ListingSerializer.create')
        title = validated_data['title']

        listing = models.Listing(title=validated_data['title'],
            category=validated_data['category'])

        listing.save()

        if 'owners' in validated_data:
            logger.debug('owners: %s' % validated_data['owners'])
            for owner in validated_data['owners']:
                print ('adding owner: %s' % owner)
                listing.owners.add(owner)
        return listing