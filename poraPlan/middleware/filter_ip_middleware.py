class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    @staticmethod
    def process_response(self, request, response):
        response.context_data['notification_count'] = 'We changed the title'
        return response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        return response
        # Code to be executed for each request/response after
        # the view is called.
