from django.shortcuts import render
from rest_framework import views, permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Reference, Manager, Partner
from .serializers import ReferenceSerializer, ManagerSerializer, PartnerSerializer
from .validators import namfarsi, likert, namOrnull
from django.core.exceptions import ValidationError


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    # permission_classes = (permissions.BasePermission,)
    http_method_names = ['post', 'get']

    @action(detail=True, methods=['POST'])
    def manager_reference(self, request, pk=None):
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

    @action(detail=True, methods=['POST'])
    def partner_reference(self, request, pk=None):
        if 'reference' in request.data:
            try:
                reference = Reference.objects.get(id=pk)
                job = namfarsi(request.data['job'])
                detail = namfarsi(request.data['detail'])
                success = namfarsi(request.data['success'])
                creativity = namfarsi(request.data['creativity'])
                teamwork = namfarsi(request.data['teamwork'])
                strong = namfarsi(request.data['strong'])
                improve = namfarsi(request.data['improve'])
                separation = namfarsi(request.data['separation'])
                suggest = likert(request.data['suggest'])
                point = namfarsi(request.data['point'])

                Partner.objects.create(reference=reference, job=job, detail=detail, success=success, creativity=creativity, teamwork=teamwork,
                                       strong=strong, improve=improve, separation=separation, suggest=suggest, point=point)

                response = {'message': 'success'}
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


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    http_method_names = ['get']


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    http_method_names = ['get']
