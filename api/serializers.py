from rest_framework import serializers
from .models import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('id', 'email', 'codemelli', 'm_name', 'm_email',
                  'm_mobile', 'p_name', 'p_email', 'p_mobile')
