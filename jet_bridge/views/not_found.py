from jet_bridge.views.base.api import APIView


class NotFoundHandler(APIView):

    def write_error(self, status_code, **kwargs):
        self.set_status(404)
        self.finish(
            f'<h1>Not Found</h1><p>The requested URL {self.request.uri} was not found on this server.</p>'
        )
