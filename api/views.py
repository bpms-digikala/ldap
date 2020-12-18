from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reference
from .serializers import ReferenceSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    http_method_names = ['post', 'get']

    # @action(detail=True, methods=['POST'])
    # def post_reference(self, request, pk=None):
    #     response = {'message': 'done'}
    #     return Response(response, status=status.HTTP_200_OK)
