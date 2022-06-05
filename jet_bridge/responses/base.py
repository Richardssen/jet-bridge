import json

from jet_bridge import encoders


class Response(object):
    headers = {'Content-Type': 'application/json'}
    encoder_class = encoders.JSONEncoder

    def __init__(self, data=None, status=None, headers=None, exception=False, content_type=None):
        self.data = data
        self.status = status
        self.exception = exception
        self.content_type = content_type

        if headers:
            self.headers.update(headers)

    def header_items(self):
        return self.headers.items() if self.headers else []

    def render(self):
        if self.data is None:
            return bytes()

        return json.dumps(
            self.data,
            cls=self.encoder_class
        )
