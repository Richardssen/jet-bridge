from six.moves.urllib_parse import quote

from jet_bridge import settings
from jet_bridge.views.base.api import APIView


class RegisterHandler(APIView):

    def get(self, *args, **kwargs):
        token = self.get_argument('token', '')

        if settings.WEB_BASE_URL.startswith('https') and not self.request.full_url().startswith('https'):
            web_base_url = f'http{settings.WEB_BASE_URL[5:]}'
        else:
            web_base_url = settings.WEB_BASE_URL

        if token:
            url = f'{web_base_url}/projects/register/{token}'
        else:
            url = f'{web_base_url}/projects/register'

        query_string = f"referrer={quote(self.request.full_url().encode('utf8'))}"

        self.redirect(f'{url}?{query_string}')
