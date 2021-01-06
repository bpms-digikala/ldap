from .models import Reference, Manager, Partner
from .validators import namfarsi, likert, namOrnull, allowchar
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
import bleach


def insertData(request, pk, value):
    for val in request.data:
        request.data[val] = bleach.clean(str(request.data[val]))
    if 'reference' in request.data and pk == 'survey':
        try:
            ref = request.data['reference']
            if value == 'Manager':
                reference = Reference.objects.get(m_uuid=ref)
            elif value == 'Partner':
                reference = Reference.objects.get(p_uuid=ref)
            job = allowchar(request.data['job'])
            detail = allowchar(request.data['detail'])
            creativity = allowchar(request.data['creativity'])
            strong = allowchar(request.data['strong'])
            improve = namOrnull(request.data['improve'])
            separation = allowchar(request.data['separation'])
            suggest = likert(request.data['suggest'])
            point = namOrnull(request.data['point'])
            if value == 'Manager':
                Manager.objects.create(reference=reference, job=job, detail=detail, creativity=creativity,
                                       strong=strong, improve=improve, separation=separation, suggest=suggest, point=point)
            elif value == 'Partner':
                Partner.objects.create(reference=reference, job=job, detail=detail, creativity=creativity,
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
            response = {"message": "Something went wrong"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    else:
        response = {"message": "parent field isn't specified"}
        return Response(response, status=status.HTTP_404_NOT_FOUND)
