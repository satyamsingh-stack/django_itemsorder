from rest_framework import serializers
from .models import *

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields='__all__'