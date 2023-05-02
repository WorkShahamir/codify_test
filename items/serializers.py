from rest_framework import serializers

from .models import Category, Item


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
