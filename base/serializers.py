from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers

from .models import Category, Portfolio, Block


class UserSerializer(serializers.ModelSerializer):
    """
        Serialize username and password
    """

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class InsanCategory(serializers.ModelSerializer):
    """
            Here we serialize the Category
    """
    class Meta:
        model = Category
        fields = "__all__"


class InsanBlock(serializers.ModelSerializer):
    """
        Here we serialize the Blocks
    """
    class Meta:
        model = Block
        fields = "__all__"


class InsanPortfolio(serializers.ModelSerializer):
    """
        This serializer showing us
        all the data from Partfolio and Blocks
    """

    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = "__all__"

    def get_blocks(self, obj):
        blocks = Block.objects.filter(portfolio=obj)[:3]
        request = self.context.get('request')
        return {
            "blocks": InsanBlock(blocks, many=True).data,
            "all_blocks_link": request.build_absolute_uri(
                reverse('portfolio_block_list', kwargs={'portfolio_id': obj.id})
            )
        }

