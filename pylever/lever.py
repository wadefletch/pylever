"""PyLever: Python bindings for the Lever Postings API

"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .errors import *
from .posting import *


class Lever:
    def __init__(self, site_name, api_key='', max_retries=5):
        self.api_key = api_key
        self.base_url = 'https://api.lever.co/'
        self.site_name = site_name
        self.max_retries = max_retries
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Creates a request.Session object using the retry standards defined in the `Lever docs <https://github.com/lever/postings-api>`_."""
        s = requests.Session()

        retry = Retry(
            total=self.max_retries,
            read=self.max_retries,
            connect=self.max_retries,
            backoff_factor=2,  # wait 2 seconds longer each retry
            status_forcelist=(429,),
        )
        adapter = HTTPAdapter(max_retries=retry)
        s.mount('https://', adapter)

        s.headers.update({'Accept': 'application/json'})

        if self.api_key:
            s.headers.update({'Authentication': self.api_key})

        return s

    def _endpoint(self, endpoint) -> str:
        """Creates a valid URL for a given endpoint from the base URL."""
        return requests.compat.urljoin(self.base_url, endpoint)

    def list_postings(self, skip=0, limit=0, location='', commitment='', team='', department='', level='', group=''):
        """Retrieves a list of all public postings from the Lever API.

           Args:
               skip: the integer number of postings to skip from the beginning
               limit: the integer max of postings to return
               location: a string or list of strings of locations for which to return positions
               commitment: a string or list of strings of commitments for which to return positions
               team: a string or list of strings of teams for which to return positions
               department: a string or list of strings of departments for which to return positions
               level: a string or list of strings of levels for which to return positions
               group: a string or list of strings of groups for which to return positions

            Returns:
                A list of lever.Posting objects retrieved from the Lever API.
        """
        # remove params with an empty string as value
        params = {k: v for (k, v) in locals().items() if v not in ['', 0]}

        return [Posting(**posting) for posting in
                self.session.get(self._endpoint(f'/v0/postings/{self.site_name}'), params=params).json()]

    def get_posting(self, posting_id):
        """Retrieves a single posting from the Lever API.

           Args:
               posting_id: the id string of the posting to be retrieved

        """
        response = self.session.get(self._endpoint(f'/v0/postings/{self.site_name}/' + posting_id)).json()
        if 'ok' in response.keys() and response['ok'] is False:
            raise LeverError(response['error'])
        return Posting(**response)

    def apply(self, posting_id, data):
        """Submits an application to the given posting. UNTESTED AND UNDOCUMENTED! USE AT YOUR OWN RISK!"""
        response = self.session.post(self._endpoint(f'/v0/postings/{self.site_name}/{posting_id}'), data=data).json()
        if 'ok' in response.keys() and response['ok'] is False:
            raise LeverError(response['error'])
        return response['applicationId']
