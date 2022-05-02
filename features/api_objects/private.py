import base64
import hashlib
import hmac
import time
import urllib.parse

import requests as r
import requests.auth


class Auth(requests.auth.AuthBase):
    """
    Custom Authentication object to handle requests with API-Key and API-Sign with signature logic

    example usage:
    >>> auth = Auth('my app url', 'api_key', 'api secret key', 'payload')
    """
    def __init__(self, uri: str, api_key: str, api_secret: str, payload_data: str):
        # setup any auth-related data here
        self.uri = uri
        self.api_key = api_key
        self.api_secret = api_secret
        self.payload_data = payload_data

    def __call__(self, r):
        r.headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        r.headers['API-Key'] = self.api_key
        r.headers['API-Sign'] = self._get_signature(self.uri, self.payload_data, self.api_secret)

        return r

    def _get_signature(self, urlpath, data, secret):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()


class PrivApiBase:
    def __init__(self, url: str, auth):
        self.site_url: str = url
        self.auth = auth

    def _send_request(
        self, method: str, uri: str, **kwargs
    ) -> requests.Response:
        """
        Generic method to send rest api request that require custom authentication
        :param method: REST method ie: 'GET', 'POST', 'PUT', 'DELETE'
        :return: requests.Response
        """

        return r.request(
            method=method,
            url=f"{self.site_url}{uri}",
            auth=self.auth,
            **kwargs,
        )

    def send_request(self, *args, **kwargs) -> requests.Response:
        return self._send_request(*args, **kwargs)


class UserData(PrivApiBase):
    """
    Object used to send requests and obtain results from Private User Data api endpoint
    """
    def __init__(self, site_url, auth, otp=None):
        super(UserData, self).__init__(site_url, auth=auth)
        self.otp = otp

    def get_data(self, uri, payload) -> requests.Response:
        payload["nonce"] = str(int(1000 * time.time()))
        if self.otp:
            payload['otp'] = self.otp

        return self._send_request("POST", f'{uri}', data=payload)
