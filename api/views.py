from django.shortcuts import render
from rest_framework import views, permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reference, Manager, Partner
from .serializers import ReferenceSerializer, ManagerSerializer, PartnerSerializer
from .validators import namfarsi, likert, namOrnull
from django.core.exceptions import ValidationError
from django.conf import settings
import requests


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    # permission_classes = (permissions.BasePermission,)
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        if 'token' in request.data:
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': settings.SECRET_CAPTCHA,
                    'response': request.data['token'],
                }
            )
            if r.json()['success']:
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
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': settings.SECRET_CAPTCHA,
                    'response': request.data['token'],
                }
            )
            if r.json()['success']:
                if 'reference' in request.data:
                    try:
                        reference = Reference.objects.get(id=pk)
                        job = namfarsi(request.data['job'])
                        detail = namfarsi(request.data['detail'])
                        success = namfarsi(request.data['success'])
                        creativity = namfarsi(request.data['creativity'])
                        teamwork = namfarsi(request.data['teamwork'])
                        strong = namfarsi(request.data['strong'])
                        improve = namOrnull(request.data['improve'])
                        separation = namfarsi(request.data['separation'])
                        suggest = likert(request.data['suggest'])
                        point = namOrnull(request.data['point'])

                        Manager.objects.create(reference=reference, job=job, detail=detail, success=success, creativity=creativity, teamwork=teamwork,
                                               strong=strong, improve=improve, separation=separation, suggest=suggest, point=point)
                        response = {'message': "success"}
                        return Response(response, status=status.HTTP_200_OK)
                    except Reference.DoesNotExist:
                        response = {"message": "reference id isn't exist"}
                        return Response(response, status=status.HTTP_404_NOT_FOUND)
                    except ValidationError as e:
                        response = {"message": e}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    except:
                        response = {"message": "something is wrong"}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)
                else:
                    response = {"message": "parent field isn't specified"}
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={'error': 'ReCAPTCHA not verified.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(detail=True, methods=['POST'])
    def partner_reference(self, request, pk=None):
        if 'token' in request.data:
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': settings.SECRET_CAPTCHA,
                    'response': request.data['token'],
                }
            )
            if r.json()['success']:
                if 'reference' in request.data:
                    try:
                        reference = Reference.objects.get(id=pk)
                        job = namfarsi(request.data['job'])
                        detail = namfarsi(request.data['detail'])
                        success = namfarsi(request.data['success'])
                        creativity = namfarsi(request.data['creativity'])
                        teamwork = namfarsi(request.data['teamwork'])
                        strong = namfarsi(request.data['strong'])
                        improve = namOrnull(request.data['improve'])
                        separation = namfarsi(request.data['separation'])
                        suggest = likert(request.data['suggest'])
                        point = namOrnull(request.data['point'])

                        Partner.objects.create(reference=reference, job=job, detail=detail, success=success, creativity=creativity, teamwork=teamwork,
                                               strong=strong, improve=improve, separation=separation, suggest=suggest, point=point)
                        response = {'message': "success"}
                        return Response(response, status=status.HTTP_200_OK)
                    except Reference.DoesNotExist:
                        response = {"message": "reference id isn't exist"}
                        return Response(response, status=status.HTTP_404_NOT_FOUND)
                    except ValidationError as e:
                        response = {"message": e}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    except:
                        response = {"message": "something is wrong"}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)
                else:
                    response = {"message": "parent field isn't specified"}
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
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
