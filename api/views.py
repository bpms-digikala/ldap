from django.shortcuts import render
from rest_framework import views, permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reference, Manager, Partner
from .serializers import ReferenceSerializer, ManagerSerializer, PartnerSerializer
from .validators import namfarsi, likert, namOrnull
from django.core.exceptions import ValidationError
import uuid
import bleach
from .recaptcha import callRecaptcha
from .createsurvey import insertData


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    # permission_classes = (permissions.BasePermission,)
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        if 'token' in request.data:
            res = callRecaptcha(request.data['token'])
            if res.json()['success']:
                for val in request.data:
                    request.data[val] = bleach.clean(str(request.data[val]))
                man = uuid.uuid4()
                request.data['m_uuid'] = str(man)
                part = uuid.uuid4()
                request.data['p_uuid'] = str(part)
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                # headers = self.get_success_headers(serializer.data)
                response = {'message': "success"}
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=True, methods=['POST'])
    def manager_reference(self, request, pk=None):
        if 'token' in request.data:
            res = callRecaptcha(request.data['token'])
            if res.json()['success']:
                return insertData(request, pk, 'Manager')
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=True, methods=['POST'])
    def partner_reference(self, request, pk=None):
        if 'token' in request.data:
            res = callRecaptcha(request.data['token'])
            if res.json()['success']:
                return insertData(request, pk, 'Partner')
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    http_method_names = ['get']


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    http_method_names = ['get']
