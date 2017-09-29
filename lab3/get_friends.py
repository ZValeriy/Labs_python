from base_class import BaseClient
import requests


class Friends(BaseClient):
    def __init__(self, vk_id):
        self.vk_id = vk_id
    method = "friends.get"
    http_method = "?uid="
    fields = "&fields=bdate"

    def generate_url(self):
        return '{0}{1}{2}{3}{4}'.format(self.BASE_URL, self.method, self.http_method, self.vk_id, self.fields)

    def get_data(self):
        response = requests.get(self.generate_url()).json()
        return response["response"]

    def make_list(self):
        templist = []
        for i in self.get_data():
            try:
                if len(i["bdate"]) >= 8:
                    templist.append(i["bdate"])
            except Exception:
                continue
        return templist
