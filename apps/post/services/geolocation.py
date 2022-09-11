import requests
import json

from apps.post.services.exceptions import PageNotLoaded
from config import settings


class GeolocationAPI:
    @staticmethod
    def geolocation_api() -> json:
        """
        :param Anonymous user
        :return response Returned data
        """
        url = settings.URL_GEOLOCATION
        response = requests.get(url=url)

        if response.status_code != 200:
            raise PageNotLoaded

        return response.json()
