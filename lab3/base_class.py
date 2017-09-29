class BaseClient:

    BASE_URL = "https://api.vk.com/method/"
    method = None
    http_method = None

    def generate_url(self):
        return None

    def _get_data(self):
        response = None
        return response
