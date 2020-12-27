
class RemoveHeaders(object):
    def process_response(self, request, response):
        response['Server'] = ''
        return response
