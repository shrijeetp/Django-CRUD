from rest_framework import serializers

from .models import *


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerRegModel
        fields = '__all__'
