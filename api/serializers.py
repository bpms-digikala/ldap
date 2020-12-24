from rest_framework import serializers
from .models import Reference, Manager, Partner


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        # fields = ('id', 'date', 'reference', 'job', 'detail', 'success',
        #           'creativity', 'teamwork', 'strong', 'improve', 'separation', 'suggest', 'point')
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
