
from django.utils.deprecation import MiddlewareMixin


class RemoveHeaders(MiddlewareMixin):
    def process_response(self, request, response):
        del response['Server']
        return response
